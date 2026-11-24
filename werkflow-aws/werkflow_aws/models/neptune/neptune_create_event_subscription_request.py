from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .neptune_tag import NeptuneTag


class NeptuneCreateEventSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
    SnsTopicArn: StrictStr
    SourceType: StrictStr | None = None
    EventCategories: list[StrictStr] | None = None
    SourceIds: list[StrictStr] | None = None
    Enabled: StrictBool | None = None
    Tags: list[NeptuneTag] | None = None
