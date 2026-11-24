from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTListTopicRulesRequest(BaseModel):
    topic: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    ruleDisabled: StrictBool | None = None
