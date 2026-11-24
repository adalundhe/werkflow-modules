from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSRemovePermissionRequest(BaseModel):
    TopicArn: StrictStr
    Label: StrictStr
