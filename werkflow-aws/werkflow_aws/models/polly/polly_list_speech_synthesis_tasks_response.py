from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .polly_synthesis_task import PollySynthesisTask


class PollyListSpeechSynthesisTasksResponse(BaseModel):
    NextToken: StrictStr | None = None
    SynthesisTasks: list[PollySynthesisTask] | None = None
    ResponseMetadata: dict[str, Any] | None = None
