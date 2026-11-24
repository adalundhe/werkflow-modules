from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueUpdateDataQualityRulesetResponse(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Ruleset: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
