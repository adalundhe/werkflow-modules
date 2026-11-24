from __future__ import annotations
from pydantic import BaseModel
from .connect_evaluation_form_text_question_automation import ConnectEvaluationFormTextQuestionAutomation


class ConnectEvaluationFormTextQuestionProperties(BaseModel):
    Automation: ConnectEvaluationFormTextQuestionAutomation | None = None
