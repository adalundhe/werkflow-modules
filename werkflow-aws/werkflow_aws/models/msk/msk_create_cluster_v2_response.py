from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MSKCreateClusterV2Response(BaseModel):
    ClusterArn: StrictStr | None = None
    ClusterName: StrictStr | None = None
    State: StrictStr | None = None
    ClusterType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
