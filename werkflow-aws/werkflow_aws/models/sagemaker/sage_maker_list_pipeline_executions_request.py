from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListPipelineExecutionsRequest(BaseModel):
    PipelineName: StrictStr
    CreatedAfter: datetime.datetime | StrictStr | None = None
    CreatedBefore: datetime.datetime | StrictStr | None = None
    SortBy: Literal['CreationTime', 'PipelineExecutionArn'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    PipelineVersionAlias: StrictStr | None = None
