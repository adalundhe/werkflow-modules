from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQDescribeConfigurationRevisionRequest(BaseModel):
    ConfigurationId: StrictStr
    ConfigurationRevision: StrictStr
