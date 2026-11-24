from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_analytics_metadata_type import CognitoIDPAnalyticsMetadataType
from .cognito_idp_attribute_type import CognitoIDPAttributeType
from .cognito_idp_user_context_data_type import CognitoIDPUserContextDataType


class CognitoIDPSignUpRequest(BaseModel):
    ClientId: StrictStr
    Username: StrictStr
    SecretHash: StrictStr | None = None
    Password: StrictStr | None = None
    UserAttributes: list[CognitoIDPAttributeType] | None = None
    ValidationData: list[CognitoIDPAttributeType] | None = None
    AnalyticsMetadata: CognitoIDPAnalyticsMetadataType | None = None
    UserContextData: CognitoIDPUserContextDataType | None = None
    ClientMetadata: dict[StrictStr, StrictStr] | None = None
