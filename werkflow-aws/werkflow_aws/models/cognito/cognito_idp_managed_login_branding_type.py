from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .cognito_idp_asset_type import CognitoIDPAssetType
from .cognito_idp_document import CognitoIDPDocument


class CognitoIDPManagedLoginBrandingType(BaseModel):
    ManagedLoginBrandingId: StrictStr | None = None
    UserPoolId: StrictStr | None = None
    UseCognitoProvidedValues: StrictBool | None = None
    Settings: CognitoIDPDocument | None = None
    Assets: list[CognitoIDPAssetType] | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
