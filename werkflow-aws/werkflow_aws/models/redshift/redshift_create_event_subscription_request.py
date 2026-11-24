from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftCreateEventSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
    SnsTopicArn: StrictStr
    SourceType: StrictStr | None = None
    SourceIds: list[StrictStr] | None = None
    EventCategories: list[StrictStr] | None = None
    Severity: StrictStr | None = None
    Enabled: StrictBool | None = None
    Tags: list[RedshiftTag] | None = None
