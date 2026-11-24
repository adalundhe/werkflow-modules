from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .polly_synthesis_task import PollySynthesisTask


class PollyGetSpeechSynthesisTaskResponse(BaseModel):
    SynthesisTask: PollySynthesisTask | None = None
    ResponseMetadata: dict[str, Any] | None = None
