from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class PollyListSpeechSynthesisTasksRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Status: Literal['scheduled', 'inProgress', 'completed', 'failed'] | None = None
