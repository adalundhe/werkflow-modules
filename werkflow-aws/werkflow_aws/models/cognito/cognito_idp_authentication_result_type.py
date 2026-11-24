from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cognito_idp_new_device_metadata_type import CognitoIDPNewDeviceMetadataType


class CognitoIDPAuthenticationResultType(BaseModel):
    AccessToken: StrictStr | None = None
    ExpiresIn: StrictInt | None = None
    TokenType: StrictStr | None = None
    RefreshToken: StrictStr | None = None
    IdToken: StrictStr | None = None
    NewDeviceMetadata: CognitoIDPNewDeviceMetadataType | None = None
