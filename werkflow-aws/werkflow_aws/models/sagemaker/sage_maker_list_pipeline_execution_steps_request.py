from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListPipelineExecutionStepsRequest(BaseModel):
    PipelineExecutionArn: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
