from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class ManagedBlockchainMemberSummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    IsOwned: StrictBool | None = None
    Arn: StrictStr | None = None
