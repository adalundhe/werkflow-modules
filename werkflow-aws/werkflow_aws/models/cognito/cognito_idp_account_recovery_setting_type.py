from __future__ import annotations
from pydantic import BaseModel
from .cognito_idp_recovery_option_type import CognitoIDPRecoveryOptionType


class CognitoIDPAccountRecoverySettingType(BaseModel):
    RecoveryMechanisms: list[CognitoIDPRecoveryOptionType] | None = None
