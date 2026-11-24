from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockRuntimeListAsyncInvokesRequest(BaseModel):
    submitTimeAfter: datetime.datetime | StrictStr | None = None
    submitTimeBefore: datetime.datetime | StrictStr | None = None
    statusEquals: Literal['InProgress', 'Completed', 'Failed'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sortBy: Literal['SubmissionTime'] | None = None
    sortOrder: Literal['Ascending', 'Descending'] | None = None
