from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_sensitive_data_detections import SecurityHubSensitiveDataDetections


class SecurityHubSensitiveDataResult(BaseModel):
    Category: StrictStr | None = None
    Detections: list[SecurityHubSensitiveDataDetections] | None = None
    TotalCount: StrictInt | None = None
