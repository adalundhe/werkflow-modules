from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MSKUpdateBrokerTypeResponse(BaseModel):
    ClusterArn: StrictStr | None = None
    ClusterOperationArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
