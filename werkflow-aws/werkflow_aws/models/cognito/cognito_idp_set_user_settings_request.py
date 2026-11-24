from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idpmfa_option_type import CognitoIDPMFAOptionType


class CognitoIDPSetUserSettingsRequest(BaseModel):
    AccessToken: StrictStr
    MFAOptions: list[CognitoIDPMFAOptionType]
