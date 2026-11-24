from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTPublishFindingToSnsParams(BaseModel):
    topicArn: StrictStr | None = None
