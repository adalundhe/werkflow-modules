from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_subscription_target_form import DataZoneSubscriptionTargetForm


class DataZoneSubscriptionTargetSummary(BaseModel):
    id: StrictStr | None = None
    authorizedPrincipals: list[StrictStr] | None = None
    domainId: StrictStr | None = None
    projectId: StrictStr | None = None
    environmentId: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    manageAccessRole: StrictStr | None = None
    applicableAssetTypes: list[StrictStr] | None = None
    subscriptionTargetConfig: list[DataZoneSubscriptionTargetForm] | None = None
    provider: StrictStr | None = None
    subscriptionGrantCreationMode: StrictStr | None = None
