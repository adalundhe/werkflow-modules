from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudWatchLogsPutIntegrationResponse(BaseModel):
    integrationName: StrictStr | None = None
    integrationStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
