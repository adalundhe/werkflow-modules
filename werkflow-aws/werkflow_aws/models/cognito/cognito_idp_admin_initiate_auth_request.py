from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cognito_idp_analytics_metadata_type import CognitoIDPAnalyticsMetadataType
from .cognito_idp_context_data_type import CognitoIDPContextDataType


class CognitoIDPAdminInitiateAuthRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr
    AuthFlow: Literal['USER_SRP_AUTH', 'REFRESH_TOKEN_AUTH', 'REFRESH_TOKEN', 'CUSTOM_AUTH', 'ADMIN_NO_SRP_AUTH', 'USER_PASSWORD_AUTH', 'ADMIN_USER_PASSWORD_AUTH', 'USER_AUTH']
    AuthParameters: dict[StrictStr, StrictStr] | None = None
    ClientMetadata: dict[StrictStr, StrictStr] | None = None
    AnalyticsMetadata: CognitoIDPAnalyticsMetadataType | None = None
    ContextData: CognitoIDPContextDataType | None = None
    Session: StrictStr | None = None
