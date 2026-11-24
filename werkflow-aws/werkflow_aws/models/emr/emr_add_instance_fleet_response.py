from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EMRAddInstanceFleetResponse(BaseModel):
    ClusterId: StrictStr | None = None
    InstanceFleetId: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
