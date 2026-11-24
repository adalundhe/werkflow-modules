from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EventBridgeListRuleNamesByTargetResponse(BaseModel):
    RuleNames: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
