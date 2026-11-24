from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQUpdateConfigurationRequest(BaseModel):
    ConfigurationId: StrictStr
    Data: StrictStr
    Description: StrictStr | None = None
