from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_subscription_target_form import DataZoneSubscriptionTargetForm


class DataZoneCreateSubscriptionTargetRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentIdentifier: StrictStr
    name: StrictStr
    type: StrictStr
    subscriptionTargetConfig: list[DataZoneSubscriptionTargetForm]
    authorizedPrincipals: list[StrictStr]
    manageAccessRole: StrictStr
    applicableAssetTypes: list[StrictStr]
    provider: StrictStr | None = None
    clientToken: StrictStr | None = None
    subscriptionGrantCreationMode: Literal['AUTOMATIC', 'MANUAL'] | None = None
