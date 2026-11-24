from __future__ import annotations
from pydantic import BaseModel
from .cognito_idp_account_takeover_actions_type import CognitoIDPAccountTakeoverActionsType
from .cognito_idp_notify_configuration_type import CognitoIDPNotifyConfigurationType


class CognitoIDPAccountTakeoverRiskConfigurationType(BaseModel):
    NotifyConfiguration: CognitoIDPNotifyConfigurationType | None = None
    Actions: CognitoIDPAccountTakeoverActionsType | None = None
