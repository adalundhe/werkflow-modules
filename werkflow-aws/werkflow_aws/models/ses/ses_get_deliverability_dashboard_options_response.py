from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .ses_domain_deliverability_tracking_option import SESDomainDeliverabilityTrackingOption


class SESGetDeliverabilityDashboardOptionsResponse(BaseModel):
    DashboardEnabled: StrictBool | None = None
    SubscriptionExpiryDate: datetime.datetime | StrictStr | None = None
    AccountStatus: StrictStr | None = None
    ActiveSubscribedDomains: list[SESDomainDeliverabilityTrackingOption] | None = None
    PendingExpirationSubscribedDomains: list[SESDomainDeliverabilityTrackingOption] | None = None
    ResponseMetadata: dict[str, Any] | None = None
