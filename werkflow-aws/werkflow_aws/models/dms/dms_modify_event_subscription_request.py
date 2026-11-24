from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DMSModifyEventSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
    SnsTopicArn: StrictStr | None = None
    SourceType: StrictStr | None = None
    EventCategories: list[StrictStr] | None = None
    Enabled: StrictBool | None = None
