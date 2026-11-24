from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSAddPermissionRequest(BaseModel):
    QueueUrl: StrictStr
    Label: StrictStr
    AWSAccountIds: list[StrictStr]
    Actions: list[StrictStr]
