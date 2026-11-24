from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_analytics_metadata_type import CognitoIDPAnalyticsMetadataType
from .cognito_idp_user_context_data_type import CognitoIDPUserContextDataType


class CognitoIDPResendConfirmationCodeRequest(BaseModel):
    ClientId: StrictStr
    Username: StrictStr
    SecretHash: StrictStr | None = None
    UserContextData: CognitoIDPUserContextDataType | None = None
    AnalyticsMetadata: CognitoIDPAnalyticsMetadataType | None = None
    ClientMetadata: dict[StrictStr, StrictStr] | None = None
