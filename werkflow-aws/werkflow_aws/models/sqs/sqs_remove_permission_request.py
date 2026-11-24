from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSRemovePermissionRequest(BaseModel):
    QueueUrl: StrictStr
    Label: StrictStr
