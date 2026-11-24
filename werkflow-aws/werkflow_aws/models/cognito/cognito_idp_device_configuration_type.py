from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CognitoIDPDeviceConfigurationType(BaseModel):
    ChallengeRequiredOnNewDevice: StrictBool | None = None
    DeviceOnlyRememberedOnUserPrompt: StrictBool | None = None
