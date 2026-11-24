from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListCandidatesForAutoMLJobRequest(BaseModel):
    AutoMLJobName: StrictStr
    StatusEquals: Literal['Completed', 'InProgress', 'Failed', 'Stopped', 'Stopping'] | None = None
    CandidateNameEquals: StrictStr | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    SortBy: Literal['CreationTime', 'Status', 'FinalObjectiveMetricValue'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
