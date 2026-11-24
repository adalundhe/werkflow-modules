from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_usage_profile_definition import GlueUsageProfileDefinition


class GlueListUsageProfilesResponse(BaseModel):
    Profiles: list[GlueUsageProfileDefinition] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
