from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .dms_tag import DMSTag


class DMSCreateEventSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
    SnsTopicArn: StrictStr
    SourceType: StrictStr | None = None
    EventCategories: list[StrictStr] | None = None
    SourceIds: list[StrictStr] | None = None
    Enabled: StrictBool | None = None
    Tags: list[DMSTag] | None = None
