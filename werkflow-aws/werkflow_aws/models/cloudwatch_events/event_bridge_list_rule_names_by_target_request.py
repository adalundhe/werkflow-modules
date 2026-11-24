from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeListRuleNamesByTargetRequest(BaseModel):
    TargetArn: StrictStr
    EventBusName: StrictStr | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
