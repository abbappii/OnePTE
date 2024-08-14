
import random
from .models import SSTScoring, ROScoring, RMMCQScoring

def score_sst_answer(answer):
    sst_question = answer.sst_question

    # Fake scoring mechanism as per requirements (random score)
    content_score = random.randint(0, 2)
    form_score = random.randint(0, 2)
    grammar_score = random.randint(0, 2)
    vocabulary_score = random.randint(0, 2)
    spelling_score = random.randint(0, 2)
    total_raw_score = content_score + form_score + grammar_score + vocabulary_score + spelling_score

    normalized_score = min(10, total_raw_score)
    answer.score = normalized_score
    answer.save()

    SSTScoring.objects.create(
        answer=answer,
        content_score=content_score,
        form_score=form_score,
        grammar_score=grammar_score,
        vocabulary_score=vocabulary_score,
        spelling_score=spelling_score,
        total_score=total_raw_score
    )

def score_ro_answer(answer):
    ro_question = answer.ro_question

    correct_pairs = evaluate_correct_pairs(answer.ro_answer, ro_question.correct_order)
    total_score = correct_pairs  # Each correct pair counts as one point

    ROScoring.objects.create(
        answer=answer,
        correct_pairs=correct_pairs,
        total_score=total_score
    )

    answer.score = total_score
    answer.save()

def score_rmmcq_answer(answer):
    rmmcq_question = answer.rmmcq_question

    correct_choices, incorrect_choices = evaluate_choices(answer.rmmcq_answer, rmmcq_question.correct_options)
    total_score = max(0, correct_choices - incorrect_choices)  # Ensure score isn't negative

    RMMCQScoring.objects.create(
        answer=answer,
        correct_choices=correct_choices,
        incorrect_choices=incorrect_choices,
        total_score=total_score
    )

    answer.score = total_score
    answer.save()

def evaluate_correct_pairs(student_answer, correct_order):
    correct_pairs = sum([1 for i in range(len(student_answer) - 1) if student_answer[i] == correct_order[i]])
    return correct_pairs

def evaluate_choices(student_answer, correct_choices):
    correct_choices_count = len([choice for choice in student_answer if choice in correct_choices])
    incorrect_choices_count = len([choice for choice in student_answer if choice not in correct_choices])
    return correct_choices_count, incorrect_choices_count
