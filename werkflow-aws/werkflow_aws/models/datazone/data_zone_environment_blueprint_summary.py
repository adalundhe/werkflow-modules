from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_provisioning_properties import DataZoneProvisioningProperties


class DataZoneEnvironmentBlueprintSummary(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    provider: StrictStr | None = None
    provisioningProperties: DataZoneProvisioningProperties | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    blueprintCategory: StrictStr | None = None
