from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RedshiftModifyEventSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
    SnsTopicArn: StrictStr | None = None
    SourceType: StrictStr | None = None
    SourceIds: list[StrictStr] | None = None
    EventCategories: list[StrictStr] | None = None
    Severity: StrictStr | None = None
    Enabled: StrictBool | None = None
