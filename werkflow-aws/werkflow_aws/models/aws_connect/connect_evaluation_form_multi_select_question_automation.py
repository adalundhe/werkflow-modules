from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_form_multi_select_question_automation_option import ConnectEvaluationFormMultiSelectQuestionAutomationOption
from .connect_evaluation_form_question_automation_answer_source import ConnectEvaluationFormQuestionAutomationAnswerSource


class ConnectEvaluationFormMultiSelectQuestionAutomation(BaseModel):
    Options: list[ConnectEvaluationFormMultiSelectQuestionAutomationOption] | None = None
    DefaultOptionRefIds: list[StrictStr] | None = None
    AnswerSource: ConnectEvaluationFormQuestionAutomationAnswerSource | None = None
