from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class TranscribeListTranscriptionJobsRequest(BaseModel):
    Status: Literal['QUEUED', 'IN_PROGRESS', 'FAILED', 'COMPLETED'] | None = None
    JobNameContains: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
