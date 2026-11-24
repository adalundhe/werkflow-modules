from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruSnsChannelConfig(BaseModel):
    TopicArn: StrictStr | None = None
