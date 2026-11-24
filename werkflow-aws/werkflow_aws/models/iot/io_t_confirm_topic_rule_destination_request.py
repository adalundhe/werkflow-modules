from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTConfirmTopicRuleDestinationRequest(BaseModel):
    confirmationToken: StrictStr
