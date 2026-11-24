from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ManagedBlockchainNetworkSummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Framework: StrictStr | None = None
    FrameworkVersion: StrictStr | None = None
    Status: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    Arn: StrictStr | None = None
