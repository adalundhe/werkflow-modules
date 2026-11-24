from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_subscribed_listing import DataZoneSubscribedListing
from .data_zone_subscribed_principal import DataZoneSubscribedPrincipal


class DataZoneSubscriptionSummary(BaseModel):
    id: StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedBy: StrictStr | None = None
    domainId: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    subscribedPrincipal: DataZoneSubscribedPrincipal | None = None
    subscribedListing: DataZoneSubscribedListing | None = None
    subscriptionRequestId: StrictStr | None = None
    retainPermissions: StrictBool | None = None
