from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_granted_entity import DataZoneGrantedEntity
from .data_zone_subscribed_asset import DataZoneSubscribedAsset


class DataZoneUpdateSubscriptionGrantStatusResponse(BaseModel):
    id: StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedBy: StrictStr | None = None
    domainId: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    environmentId: StrictStr | None = None
    subscriptionTargetId: StrictStr | None = None
    grantedEntity: DataZoneGrantedEntity | None = None
    status: StrictStr | None = None
    assets: list[DataZoneSubscribedAsset] | None = None
    subscriptionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
