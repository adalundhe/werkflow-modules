from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_policy import GluePolicy


class GlueGetResourcePoliciesResponse(BaseModel):
    GetResourcePoliciesResponseList: list[GluePolicy] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
