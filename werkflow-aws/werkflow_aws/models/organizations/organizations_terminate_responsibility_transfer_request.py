from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class OrganizationsTerminateResponsibilityTransferRequest(BaseModel):
    Id: StrictStr
    EndTimestamp: datetime.datetime | StrictStr | None = None
