from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_task_run_properties import GlueTaskRunProperties


class GlueTaskRun(BaseModel):
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
