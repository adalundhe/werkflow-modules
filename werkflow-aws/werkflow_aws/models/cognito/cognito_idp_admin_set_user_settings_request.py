from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idpmfa_option_type import CognitoIDPMFAOptionType


class CognitoIDPAdminSetUserSettingsRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    MFAOptions: list[CognitoIDPMFAOptionType]
