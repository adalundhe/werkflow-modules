from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ManagedBlockchainNodeSummary(BaseModel):
    Id: StrictStr | None = None
    Status: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    InstanceType: StrictStr | None = None
    Arn: StrictStr | None = None
