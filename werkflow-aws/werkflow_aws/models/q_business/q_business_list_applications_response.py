from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_application import QBusinessApplication


class QBusinessListApplicationsResponse(BaseModel):
    nextToken: StrictStr | None = None
    applications: list[QBusinessApplication] | None = None
    ResponseMetadata: dict[str, Any] | None = None
