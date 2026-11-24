from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2GetIpamAddressHistoryRequest(BaseModel):
    Cidr: StrictStr
    IpamScopeId: StrictStr
    DryRun: StrictBool | None = None
    VpcId: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
