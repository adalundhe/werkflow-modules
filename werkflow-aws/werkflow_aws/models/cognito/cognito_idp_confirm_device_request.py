from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_device_secret_verifier_config_type import CognitoIDPDeviceSecretVerifierConfigType


class CognitoIDPConfirmDeviceRequest(BaseModel):
    AccessToken: StrictStr
    DeviceKey: StrictStr
    DeviceSecretVerifierConfig: CognitoIDPDeviceSecretVerifierConfigType | None = None
    DeviceName: StrictStr | None = None
