from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSAddPermissionRequest(BaseModel):
    TopicArn: StrictStr
    Label: StrictStr
    AWSAccountId: list[StrictStr]
    ActionName: list[StrictStr]
