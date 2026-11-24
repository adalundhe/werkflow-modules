from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_answer_input import ConnectEvaluationAnswerInput
from .connect_evaluation_note import ConnectEvaluationNote
from .connect_evaluator_user_union import ConnectEvaluatorUserUnion


class ConnectSubmitContactEvaluationRequest(BaseModel):
    InstanceId: StrictStr
    EvaluationId: StrictStr
    Answers: dict[StrictStr, ConnectEvaluationAnswerInput] | None = None
    Notes: dict[StrictStr, ConnectEvaluationNote] | None = None
    SubmittedBy: ConnectEvaluatorUserUnion | None = None
