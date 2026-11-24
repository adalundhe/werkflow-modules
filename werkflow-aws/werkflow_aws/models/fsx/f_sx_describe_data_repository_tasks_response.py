from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_data_repository_task import FSxDataRepositoryTask


class FSxDescribeDataRepositoryTasksResponse(BaseModel):
    DataRepositoryTasks: list[FSxDataRepositoryTask] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
