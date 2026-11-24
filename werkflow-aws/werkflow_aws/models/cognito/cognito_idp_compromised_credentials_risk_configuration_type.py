from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_compromised_credentials_actions_type import CognitoIDPCompromisedCredentialsActionsType


class CognitoIDPCompromisedCredentialsRiskConfigurationType(BaseModel):
    EventFilter: list[StrictStr] | None = None
    Actions: CognitoIDPCompromisedCredentialsActionsType | None = None
