from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PollyGetSpeechSynthesisTaskRequest(BaseModel):
    TaskId: StrictStr
