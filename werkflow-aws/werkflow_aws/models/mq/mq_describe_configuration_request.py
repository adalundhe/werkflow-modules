from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQDescribeConfigurationRequest(BaseModel):
    ConfigurationId: StrictStr
