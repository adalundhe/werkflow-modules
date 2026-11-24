from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockListEvaluationJobsRequest(BaseModel):
    creationTimeAfter: datetime.datetime | StrictStr | None = None
    creationTimeBefore: datetime.datetime | StrictStr | None = None
    statusEquals: Literal['InProgress', 'Completed', 'Failed', 'Stopping', 'Stopped', 'Deleting'] | None = None
    applicationTypeEquals: Literal['ModelEvaluation', 'RagEvaluation'] | None = None
    nameContains: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sortBy: Literal['CreationTime'] | None = None
    sortOrder: Literal['Ascending', 'Descending'] | None = None
