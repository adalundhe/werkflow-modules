from __future__ import annotations
from pydantic import BaseModel
from .connect_evaluation_form_question import ConnectEvaluationFormQuestion
from .connect_evaluation_form_section import ConnectEvaluationFormSection


class ConnectEvaluationFormItem(BaseModel):
    Section: ConnectEvaluationFormSection | None = None
    Question: ConnectEvaluationFormQuestion | None = None
