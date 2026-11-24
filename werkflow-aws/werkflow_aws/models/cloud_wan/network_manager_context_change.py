from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_context_entry import NetworkManagerContextEntry


class NetworkManagerContextChange(BaseModel):
    ChangeType: StrictStr | None = None
    Context: NetworkManagerContextEntry | None = None
