from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_data_repository_task_filter import FSxDataRepositoryTaskFilter


class FSxDescribeDataRepositoryTasksRequest(BaseModel):
    TaskIds: list[StrictStr] | None = None
    Filters: list[FSxDataRepositoryTaskFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
