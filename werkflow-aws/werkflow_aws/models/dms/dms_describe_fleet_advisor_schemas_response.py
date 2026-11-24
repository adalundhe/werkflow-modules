from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_schema_response import DMSSchemaResponse


class DMSDescribeFleetAdvisorSchemasResponse(BaseModel):
    FleetAdvisorSchemas: list[DMSSchemaResponse] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
