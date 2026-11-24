from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_service_options import OpenSearchServiceOptions


class OpenSearchAuthorizedPrincipal(BaseModel):
    PrincipalType: StrictStr | None = None
    Principal: StrictStr | None = None
    ServiceOptions: OpenSearchServiceOptions | None = None
