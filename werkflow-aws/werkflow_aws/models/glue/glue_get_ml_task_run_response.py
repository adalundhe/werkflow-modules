from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_task_run_properties import GlueTaskRunProperties


class GlueGetMLTaskRunResponse(BaseModel):
    TransformId: StrictStr | None = None
    TaskRunId: StrictStr | None = None
    Status: StrictStr | None = None
    LogGroupName: StrictStr | None = None
    Properties: GlueTaskRunProperties | None = None
    ErrorString: StrictStr | None = None
    StartedOn: datetime.datetime | StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
    CompletedOn: datetime.datetime | StrictStr | None = None
    ExecutionTime: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
