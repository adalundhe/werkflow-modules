from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cognito_idp_asset_type import CognitoIDPAssetType
from .cognito_idp_document import CognitoIDPDocument


class CognitoIDPUpdateManagedLoginBrandingRequest(BaseModel):
    UserPoolId: StrictStr | None = None
    ManagedLoginBrandingId: StrictStr | None = None
    UseCognitoProvidedValues: StrictBool | None = None
    Settings: CognitoIDPDocument | None = None
    Assets: list[CognitoIDPAssetType] | None = None
