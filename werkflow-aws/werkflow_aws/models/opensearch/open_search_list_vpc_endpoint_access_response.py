from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_authorized_principal import OpenSearchAuthorizedPrincipal


class OpenSearchListVpcEndpointAccessResponse(BaseModel):
    AuthorizedPrincipalList: list[OpenSearchAuthorizedPrincipal] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
