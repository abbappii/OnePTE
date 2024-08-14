from celery import shared_task
from .models import Answer
from .utils import score_sst_answer, score_ro_answer, score_rmmcq_answer

@shared_task
def score_answer_task(answer_id):
    try:
        answer = Answer.objects.get(id=answer_id)

        if answer.sst_question:
            score_sst_answer(answer)
        elif answer.ro_question:
            score_ro_answer(answer)
        elif answer.rmmcq_question:
            score_rmmcq_answer(answer)

    except Answer.DoesNotExist:
        pass