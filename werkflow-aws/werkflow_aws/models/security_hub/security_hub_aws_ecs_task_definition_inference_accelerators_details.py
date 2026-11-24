from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsTaskDefinitionInferenceAcceleratorsDetails(BaseModel):
    DeviceName: StrictStr | None = None
    DeviceType: StrictStr | None = None
