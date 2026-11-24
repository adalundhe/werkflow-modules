from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cognito_idp_analytics_metadata_type import CognitoIDPAnalyticsMetadataType
from .cognito_idp_context_data_type import CognitoIDPContextDataType


class CognitoIDPAdminRespondToAuthChallengeRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr
    ChallengeName: Literal['SMS_MFA', 'EMAIL_OTP', 'SOFTWARE_TOKEN_MFA', 'SELECT_MFA_TYPE', 'MFA_SETUP', 'PASSWORD_VERIFIER', 'CUSTOM_CHALLENGE', 'SELECT_CHALLENGE', 'DEVICE_SRP_AUTH', 'DEVICE_PASSWORD_VERIFIER', 'ADMIN_NO_SRP_AUTH', 'NEW_PASSWORD_REQUIRED', 'SMS_OTP', 'PASSWORD', 'WEB_AUTHN', 'PASSWORD_SRP']
    ChallengeResponses: dict[StrictStr, StrictStr] | None = None
    Session: StrictStr | None = None
    AnalyticsMetadata: CognitoIDPAnalyticsMetadataType | None = None
    ContextData: CognitoIDPContextDataType | None = None
    ClientMetadata: dict[StrictStr, StrictStr] | None = None
