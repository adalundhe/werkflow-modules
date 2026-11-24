from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCreateEventSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
    SnsTopicArn: StrictStr
    SourceType: StrictStr | None = None
    EventCategories: list[StrictStr] | None = None
    SourceIds: list[StrictStr] | None = None
    Enabled: StrictBool | None = None
    Tags: list[RDSTagModel] | None = None
