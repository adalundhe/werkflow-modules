from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDestination(BaseModel):
    destinationName: StrictStr | None = None
    targetArn: StrictStr | None = None
    roleArn: StrictStr | None = None
    accessPolicy: StrictStr | None = None
    arn: StrictStr | None = None
    creationTime: StrictInt | None = None
