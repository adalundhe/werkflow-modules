from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_resource_set_summary import FMSResourceSetSummary


class FMSListResourceSetsResponse(BaseModel):
    ResourceSets: list[FMSResourceSetSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
