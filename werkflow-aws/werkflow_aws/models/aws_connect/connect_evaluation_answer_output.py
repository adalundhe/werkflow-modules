from __future__ import annotations
from pydantic import BaseModel
from .connect_evaluation_answer_data import ConnectEvaluationAnswerData
from .connect_evaluation_suggested_answer import ConnectEvaluationSuggestedAnswer


class ConnectEvaluationAnswerOutput(BaseModel):
    Value: ConnectEvaluationAnswerData | None = None
    SystemSuggestedValue: ConnectEvaluationAnswerData | None = None
    SuggestedAnswers: list[ConnectEvaluationSuggestedAnswer] | None = None
