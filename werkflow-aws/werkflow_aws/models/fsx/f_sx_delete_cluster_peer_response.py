from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class FSxDeleteClusterPeerResponse(BaseModel):
    ClusterPeerId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
