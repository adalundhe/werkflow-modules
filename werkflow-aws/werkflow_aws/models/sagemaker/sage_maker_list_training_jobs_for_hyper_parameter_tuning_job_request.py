from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListTrainingJobsForHyperParameterTuningJobRequest(BaseModel):
    HyperParameterTuningJobName: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    StatusEquals: Literal['InProgress', 'Completed', 'Failed', 'Stopping', 'Stopped', 'Deleting'] | None = None
    SortBy: Literal['Name', 'CreationTime', 'Status', 'FinalObjectiveMetricValue'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
