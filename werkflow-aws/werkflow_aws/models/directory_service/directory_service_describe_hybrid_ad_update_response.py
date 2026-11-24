from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_hybrid_update_activities import DirectoryServiceHybridUpdateActivities


class DirectoryServiceDescribeHybridADUpdateResponse(BaseModel):
    UpdateActivities: DirectoryServiceHybridUpdateActivities | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
