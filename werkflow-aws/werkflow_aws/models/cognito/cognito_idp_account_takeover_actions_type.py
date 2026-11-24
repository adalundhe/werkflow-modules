from __future__ import annotations
from pydantic import BaseModel
from .cognito_idp_account_takeover_action_type import CognitoIDPAccountTakeoverActionType


class CognitoIDPAccountTakeoverActionsType(BaseModel):
    LowAction: CognitoIDPAccountTakeoverActionType | None = None
    MediumAction: CognitoIDPAccountTakeoverActionType | None = None
    HighAction: CognitoIDPAccountTakeoverActionType | None = None
