from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_user_pool_client_description import CognitoIDPUserPoolClientDescription


class CognitoIDPListUserPoolClientsResponse(BaseModel):
    UserPoolClients: list[CognitoIDPUserPoolClientDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
