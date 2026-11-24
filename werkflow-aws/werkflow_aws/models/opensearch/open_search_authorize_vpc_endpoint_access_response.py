from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_authorized_principal import OpenSearchAuthorizedPrincipal


class OpenSearchAuthorizeVpcEndpointAccessResponse(BaseModel):
    AuthorizedPrincipal: OpenSearchAuthorizedPrincipal | None = None
    ResponseMetadata: dict[str, Any] | None = None
