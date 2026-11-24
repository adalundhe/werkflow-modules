from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_database_response import DMSDatabaseResponse


class DMSDescribeFleetAdvisorDatabasesResponse(BaseModel):
    Databases: list[DMSDatabaseResponse] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
