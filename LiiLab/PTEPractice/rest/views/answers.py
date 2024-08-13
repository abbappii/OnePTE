from rest_framework import generics
from ...models import Answer, SSTScoring, ROScoring, RMMCQScoring, SSTQuestion, ROQuestion, RMMCQQuestion
from ..serializers.answers import AnswerSerializer
import nltk
from nltk.corpus import wordnet
import Levenshtein

from textblob import TextBlob

nltk.download('wordnet')

class AnswerCreateView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.filter()

    def perform_create(self, serializer):
        user = self.request.user
        answer = serializer.save(user=user)

        if answer.sst_question:
            self._score_sst_answer(answer)
        elif answer.ro_question:
            self._score_ro_answer(answer)
        elif answer.rmmcq_question:
            self._score_rmmcq_answer(answer)

    def _score_sst_answer(self, answer):
        sst_question = SSTQuestion.objects.get(id=answer.sst_question.id)

        content_score = self._evaluate_content(answer.sst_answer, sst_question.reference_summary)
        form_score = self._evaluate_form(answer.sst_answer)
        grammar_score = self._evaluate_grammar(answer.sst_answer)
        vocabulary_score = self._evaluate_vocabulary(answer.sst_answer)
        spelling_score = self._evaluate_spelling(answer.sst_answer)
        total_raw_score = content_score + form_score + grammar_score + vocabulary_score + spelling_score

        normalized_score = min(10, total_raw_score)
        answer.score = normalized_score
        answer.save()

        answer.score = normalized_score
        answer.save()

        s = SSTScoring.objects.create(
            answer=answer,
            content_score=content_score,
            form_score=form_score,
            grammar_score=grammar_score,
            vocabulary_score=vocabulary_score,
            spelling_score=spelling_score,
            total_score=total_raw_score
        )

    def _score_ro_answer(self, answer):
        ro_question = answer.ro_question

        correct_pairs = self._evaluate_correct_pairs(answer.ro_answer, ro_question.correct_order)
        total_score = correct_pairs  # Each correct pair counts as one point

        ROScoring.objects.create(
            answer=answer,
            correct_pairs=correct_pairs,
            total_score=total_score
        )

        answer.score = total_score
        answer.save()

    def _score_rmmcq_answer(self, answer):
        rmmcq_question = answer.rmmcq_question

        correct_choices, incorrect_choices = self._evaluate_choices(answer.rmmcq_answer, rmmcq_question.correct_options)
        total_score = max(0, correct_choices - incorrect_choices)  # Ensure score isn't negative

        RMMCQScoring.objects.create(
            answer=answer,
            correct_choices=correct_choices,
            incorrect_choices=incorrect_choices,
            total_score=total_score
        )

        answer.score = total_score
        answer.save()

    def _evaluate_content(self, student_answer, reference_summary):
        similarity = self._semantic_similarity(student_answer, reference_summary)
        if similarity > 0.7:
            return 2
        elif similarity > 0.4:
            return 1
        else:
            return 0

    def _semantic_similarity(self, text1, text2):
        synsets1 = [wordnet.synsets(word) for word in text1.split()]
        synsets2 = [wordnet.synsets(word) for word in text2.split()]
        score, count = 0.0, 0

        for synset1 in synsets1:
            for synset2 in synsets2:
                if synset1 and synset2:
                    similarity = wordnet.wup_similarity(synset1[0], synset2[0])
                    if similarity:
                        score += similarity
                        count += 1
        if count > 0:
            return score / count
        else:
            return 0

    def _evaluate_form(self, answer_text):
        sentences = answer_text.split('.')
        word_count = len(answer_text.split())

        if len(sentences) > 2 and word_count > 15:
            return 2
        elif word_count > 10:
            return 1
        else:
            return 0

    def _evaluate_grammar(self, answer_text):
        blob = TextBlob(answer_text)
        corrected_text = str(blob.correct())
        grammar_score = 5 - Levenshtein.distance(answer_text, corrected_text)
        return max(2, grammar_score)  # Ensure a minimum score of 2

    def _evaluate_vocabulary(self, answer_text):
        advanced_words = ["however", "moreover", "consequently", "notwithstanding", "nonetheless"]
        score = sum([1 for word in advanced_words if word in answer_text.lower()])
        return min(2, score)  # Cap the score at 2

    def _evaluate_spelling(self, answer_text):
        words = answer_text.split()
        score = 2  # Start with full score

        for word in words:
            corrected_word = str(TextBlob(word).correct())
            distance = Levenshtein.distance(word, corrected_word)
            if distance > 0:
                score -= 0.5

        return max(0, score)

    def _evaluate_correct_pairs(self, student_answer, correct_order):
        correct_pairs = sum([1 for i in range(len(student_answer) - 1) if student_answer[i] == correct_order[i]])
        return correct_pairs

    def _evaluate_choices(self, student_answer, correct_choices):
        correct_choices_count = len([choice for choice in student_answer if choice in correct_choices])
        incorrect_choices_count = len([choice for choice in student_answer if choice not in correct_choices])
        return correct_choices_count, incorrect_choices_count

class AnswerDetailView(generics.RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
