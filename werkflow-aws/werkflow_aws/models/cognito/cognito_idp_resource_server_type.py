from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_resource_server_scope_type import CognitoIDPResourceServerScopeType


class CognitoIDPResourceServerType(BaseModel):
    UserPoolId: StrictStr | None = None
    Identifier: StrictStr | None = None
    Name: StrictStr | None = None
    Scopes: list[CognitoIDPResourceServerScopeType] | None = None
    ManagedBy: StrictStr | None = None
