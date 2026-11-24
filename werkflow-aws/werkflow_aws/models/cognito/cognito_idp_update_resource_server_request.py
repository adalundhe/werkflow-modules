from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_resource_server_scope_type import CognitoIDPResourceServerScopeType


class CognitoIDPUpdateResourceServerRequest(BaseModel):
    UserPoolId: StrictStr
    Identifier: StrictStr
    Name: StrictStr
    Scopes: list[CognitoIDPResourceServerScopeType] | None = None
