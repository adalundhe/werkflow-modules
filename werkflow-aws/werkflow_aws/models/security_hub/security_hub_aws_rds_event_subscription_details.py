from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsRdsEventSubscriptionDetails(BaseModel):
    CustSubscriptionId: StrictStr | None = None
    CustomerAwsId: StrictStr | None = None
    Enabled: StrictBool | None = None
    EventCategoriesList: list[StrictStr] | None = None
    EventSubscriptionArn: StrictStr | None = None
    SnsTopicArn: StrictStr | None = None
    SourceIdsList: list[StrictStr] | None = None
    SourceType: StrictStr | None = None
    Status: StrictStr | None = None
    SubscriptionCreationTime: StrictStr | None = None
