from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ses_inbox_placement_tracking_option import SESInboxPlacementTrackingOption


class SESDomainDeliverabilityTrackingOption(BaseModel):
    Domain: StrictStr | None = None
    SubscriptionStartDate: datetime.datetime | StrictStr | None = None
    InboxPlacementTrackingOption: SESInboxPlacementTrackingOption | None = None
