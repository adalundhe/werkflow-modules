from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_context_change import NetworkManagerContextChange


class NetworkManagerListContextChangesResponse(BaseModel):
    ContextChanges: list[NetworkManagerContextChange] | None = None
    FromVersionId: StrictStr | None = None
    ToVersionId: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
