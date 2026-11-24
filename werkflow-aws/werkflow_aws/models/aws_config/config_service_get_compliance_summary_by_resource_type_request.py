from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceGetComplianceSummaryByResourceTypeRequest(BaseModel):
    ResourceTypes: list[StrictStr] | None = None
