from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_form_single_select_question_automation import ConnectEvaluationFormSingleSelectQuestionAutomation
from .connect_evaluation_form_single_select_question_option import ConnectEvaluationFormSingleSelectQuestionOption


class ConnectEvaluationFormSingleSelectQuestionProperties(BaseModel):
    Options: list[ConnectEvaluationFormSingleSelectQuestionOption] | None = None
    DisplayAs: StrictStr | None = None
    Automation: ConnectEvaluationFormSingleSelectQuestionAutomation | None = None
