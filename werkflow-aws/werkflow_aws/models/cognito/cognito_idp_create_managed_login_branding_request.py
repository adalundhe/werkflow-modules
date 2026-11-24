from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cognito_idp_asset_type import CognitoIDPAssetType
from .cognito_idp_document import CognitoIDPDocument


class CognitoIDPCreateManagedLoginBrandingRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr
    UseCognitoProvidedValues: StrictBool | None = None
    Settings: CognitoIDPDocument | None = None
    Assets: list[CognitoIDPAssetType] | None = None
