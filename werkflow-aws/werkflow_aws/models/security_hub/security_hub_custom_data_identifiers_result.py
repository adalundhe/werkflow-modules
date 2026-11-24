from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .security_hub_custom_data_identifiers_detections import SecurityHubCustomDataIdentifiersDetections


class SecurityHubCustomDataIdentifiersResult(BaseModel):
    Detections: list[SecurityHubCustomDataIdentifiersDetections] | None = None
    TotalCount: StrictInt | None = None
