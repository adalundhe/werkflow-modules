from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .connect_evaluation_form_numeric_question_automation import ConnectEvaluationFormNumericQuestionAutomation
from .connect_evaluation_form_numeric_question_option import ConnectEvaluationFormNumericQuestionOption


class ConnectEvaluationFormNumericQuestionProperties(BaseModel):
    MinValue: StrictInt | None = None
    MaxValue: StrictInt | None = None
    Options: list[ConnectEvaluationFormNumericQuestionOption] | None = None
    Automation: ConnectEvaluationFormNumericQuestionAutomation | None = None
