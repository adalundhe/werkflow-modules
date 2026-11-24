from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_subscription_target_form import DataZoneSubscriptionTargetForm


class DataZoneUpdateSubscriptionTargetRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentIdentifier: StrictStr
    identifier: StrictStr
    name: StrictStr | None = None
    authorizedPrincipals: list[StrictStr] | None = None
    applicableAssetTypes: list[StrictStr] | None = None
    subscriptionTargetConfig: list[DataZoneSubscriptionTargetForm] | None = None
    manageAccessRole: StrictStr | None = None
    provider: StrictStr | None = None
    subscriptionGrantCreationMode: Literal['AUTOMATIC', 'MANUAL'] | None = None
