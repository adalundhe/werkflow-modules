from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_form_question_automation_answer_source import ConnectEvaluationFormQuestionAutomationAnswerSource
from .connect_evaluation_form_single_select_question_automation_option import ConnectEvaluationFormSingleSelectQuestionAutomationOption


class ConnectEvaluationFormSingleSelectQuestionAutomation(BaseModel):
    Options: list[ConnectEvaluationFormSingleSelectQuestionAutomationOption] | None = None
    DefaultOptionRefId: StrictStr | None = None
    AnswerSource: ConnectEvaluationFormQuestionAutomationAnswerSource | None = None
