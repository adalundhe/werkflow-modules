from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class IoTDescribeThingRegistrationTaskResponse(BaseModel):
    taskId: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    templateBody: StrictStr | None = None
    inputFileBucket: StrictStr | None = None
    inputFileKey: StrictStr | None = None
    roleArn: StrictStr | None = None
    status: StrictStr | None = None
    message: StrictStr | None = None
    successCount: StrictInt | None = None
    failureCount: StrictInt | None = None
    percentageProgress: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
