from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEvaluationQuestionInputDetails(BaseModel):
    TranscriptType: StrictStr | None = None
