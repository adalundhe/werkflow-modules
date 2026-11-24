from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_context_entry import NetworkManagerContextEntry


class NetworkManagerListContextsResponse(BaseModel):
    Contexts: list[NetworkManagerContextEntry] | None = None
    NextToken: StrictStr | None = None
    VersionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
