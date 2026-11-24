from __future__ import annotations
from pydantic import BaseModel, StrictBool


class LexAllowedInputTypes(BaseModel):
    allowAudioInput: StrictBool | None = None
    allowDTMFInput: StrictBool | None = None
