from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SESPutConfigurationSetReputationOptionsRequest(BaseModel):
    ConfigurationSetName: StrictStr
    ReputationMetricsEnabled: StrictBool | None = None
