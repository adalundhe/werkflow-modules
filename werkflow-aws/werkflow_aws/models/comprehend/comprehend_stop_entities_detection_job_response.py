from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ComprehendStopEntitiesDetectionJobResponse(BaseModel):
    JobId: StrictStr | None = None
    JobStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
