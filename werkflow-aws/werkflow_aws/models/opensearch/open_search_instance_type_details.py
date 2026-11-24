from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchInstanceTypeDetails(BaseModel):
    InstanceType: StrictStr | None = None
    EncryptionEnabled: StrictBool | None = None
    CognitoEnabled: StrictBool | None = None
    AppLogsEnabled: StrictBool | None = None
    AdvancedSecurityEnabled: StrictBool | None = None
    WarmEnabled: StrictBool | None = None
    InstanceRole: list[StrictStr] | None = None
    AvailabilityZones: list[StrictStr] | None = None
