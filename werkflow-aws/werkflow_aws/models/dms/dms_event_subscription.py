from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DMSEventSubscription(BaseModel):
    CustomerAwsId: StrictStr | None = None
    CustSubscriptionId: StrictStr | None = None
    SnsTopicArn: StrictStr | None = None
    Status: StrictStr | None = None
    SubscriptionCreationTime: StrictStr | None = None
    SourceType: StrictStr | None = None
    SourceIdsList: list[StrictStr] | None = None
    EventCategoriesList: list[StrictStr] | None = None
    Enabled: StrictBool | None = None
