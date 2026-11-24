from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_form_multi_select_question_automation import ConnectEvaluationFormMultiSelectQuestionAutomation
from .connect_evaluation_form_multi_select_question_option import ConnectEvaluationFormMultiSelectQuestionOption


class ConnectEvaluationFormMultiSelectQuestionProperties(BaseModel):
    Options: list[ConnectEvaluationFormMultiSelectQuestionOption] | None = None
    DisplayAs: StrictStr | None = None
    Automation: ConnectEvaluationFormMultiSelectQuestionAutomation | None = None
