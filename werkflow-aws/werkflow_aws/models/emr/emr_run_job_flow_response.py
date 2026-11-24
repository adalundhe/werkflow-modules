from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EMRRunJobFlowResponse(BaseModel):
    JobFlowId: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
