from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .open_search_service_options import OpenSearchServiceOptions


class OpenSearchRevokeVpcEndpointAccessRequest(BaseModel):
    DomainName: StrictStr
    Account: StrictStr | None = None
    Service: Literal['application.opensearchservice.amazonaws.com'] | None = None
    ServiceOptions: OpenSearchServiceOptions | None = None
