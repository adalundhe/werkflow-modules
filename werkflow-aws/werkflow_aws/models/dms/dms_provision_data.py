from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSProvisionData(BaseModel):
    ProvisionState: StrictStr | None = None
    ProvisionedCapacityUnits: StrictInt | None = None
    DateProvisioned: datetime.datetime | StrictStr | None = None
    IsNewProvisioningAvailable: StrictBool | None = None
    DateNewProvisioningDataAvailable: datetime.datetime | StrictStr | None = None
    ReasonForNewProvisioningData: StrictStr | None = None
