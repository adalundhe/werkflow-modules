from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2GetIpamRoutingPolicyRegistrationDeltasRequest(BaseModel):
    IpamInternetRegistryAssociationId: StrictStr
    DryRun: StrictBool | None = None
    DeltaId: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ChronologicalOrder: Literal['forward', 'reverse'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
