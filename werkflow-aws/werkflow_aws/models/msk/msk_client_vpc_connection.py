from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MSKClientVpcConnection(BaseModel):
    Authentication: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    VpcConnectionArn: StrictStr | None = None
    Owner: StrictStr | None = None
