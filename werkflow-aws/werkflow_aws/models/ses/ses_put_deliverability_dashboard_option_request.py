from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ses_domain_deliverability_tracking_option import SESDomainDeliverabilityTrackingOption


class SESPutDeliverabilityDashboardOptionRequest(BaseModel):
    DashboardEnabled: StrictBool
    SubscribedDomains: list[SESDomainDeliverabilityTrackingOption] | None = None
