from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ManagedGrafanaListVersionsResponse(BaseModel):
    nextToken: StrictStr | None = None
    grafanaVersions: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
