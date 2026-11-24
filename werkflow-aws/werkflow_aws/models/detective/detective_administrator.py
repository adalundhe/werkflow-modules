from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DetectiveAdministrator(BaseModel):
    AccountId: StrictStr | None = None
    GraphArn: StrictStr | None = None
    DelegationTime: datetime.datetime | StrictStr | None = None
