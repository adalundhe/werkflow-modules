from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_fleet_advisor_schema_object_response import DMSFleetAdvisorSchemaObjectResponse


class DMSDescribeFleetAdvisorSchemaObjectSummaryResponse(BaseModel):
    FleetAdvisorSchemaObjects: list[DMSFleetAdvisorSchemaObjectResponse] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
