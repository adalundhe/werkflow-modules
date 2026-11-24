from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ComprehendStartEntitiesDetectionJobResponse(BaseModel):
    JobId: StrictStr | None = None
    JobArn: StrictStr | None = None
    JobStatus: StrictStr | None = None
    EntityRecognizerArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
