from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .io_t_job_execution_status_details import IoTJobExecutionStatusDetails


class IoTJobExecution(BaseModel):
    jobId: StrictStr | None = None
    status: StrictStr | None = None
    forceCanceled: StrictBool | None = None
    statusDetails: IoTJobExecutionStatusDetails | None = None
    thingArn: StrictStr | None = None
    queuedAt: datetime.datetime | StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    executionNumber: StrictInt | None = None
    versionNumber: StrictInt | None = None
    approximateSecondsBeforeTimedOut: StrictInt | None = None
