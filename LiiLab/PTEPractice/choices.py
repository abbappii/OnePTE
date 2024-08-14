from django.db import models

class QuestionTypes(models.TextChoices):
    SST = 'SST', 'Summarize Spoken Text'
    RO = 'RO', 'Re-Order Paragraph'
    RMMCQ = 'RMMCQ', 'Reading Multiple Choice (Multiple)'
