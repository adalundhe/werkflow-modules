from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_provider_description import CognitoIDPProviderDescription


class CognitoIDPListIdentityProvidersResponse(BaseModel):
    Providers: list[CognitoIDPProviderDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
