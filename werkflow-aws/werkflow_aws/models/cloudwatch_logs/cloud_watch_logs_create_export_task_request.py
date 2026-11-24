from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr


class CloudWatchLogsCreateExportTaskRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    logGroupName: StrictStr
    from_: StrictInt = Field(alias='from')
    to: StrictInt
    destination: StrictStr
    taskName: StrictStr | None = None
    logStreamNamePrefix: StrictStr | None = None
    destinationPrefix: StrictStr | None = None
