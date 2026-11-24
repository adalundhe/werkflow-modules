from __future__ import annotations
from pydantic import BaseModel
from .connect_evaluation_answer_data import ConnectEvaluationAnswerData


class ConnectEvaluationAnswerInput(BaseModel):
    Value: ConnectEvaluationAnswerData | None = None
