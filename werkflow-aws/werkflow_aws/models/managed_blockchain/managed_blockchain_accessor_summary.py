from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ManagedBlockchainAccessorSummary(BaseModel):
    Id: StrictStr | None = None
    Type: StrictStr | None = None
    Status: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    Arn: StrictStr | None = None
    NetworkType: StrictStr | None = None
