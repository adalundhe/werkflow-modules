from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_form_output import DataZoneFormOutput
from .data_zone_subscribed_listing import DataZoneSubscribedListing
from .data_zone_subscribed_principal import DataZoneSubscribedPrincipal


class DataZoneUpdateSubscriptionRequestResponse(BaseModel):
    id: StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedBy: StrictStr | None = None
    domainId: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    requestReason: StrictStr | None = None
    subscribedPrincipals: list[DataZoneSubscribedPrincipal] | None = None
    subscribedListings: list[DataZoneSubscribedListing] | None = None
    reviewerId: StrictStr | None = None
    decisionComment: StrictStr | None = None
    existingSubscriptionId: StrictStr | None = None
    metadataForms: list[DataZoneFormOutput] | None = None
    ResponseMetadata: dict[str, Any] | None = None
