from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class RDSDBProxyEndpoint(BaseModel):
    DBProxyEndpointName: StrictStr | None = None
    DBProxyEndpointArn: StrictStr | None = None
    DBProxyName: StrictStr | None = None
    Status: StrictStr | None = None
    VpcId: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    VpcSubnetIds: list[StrictStr] | None = None
    Endpoint: StrictStr | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    TargetRole: StrictStr | None = None
    IsDefault: StrictBool | None = None
    EndpointNetworkType: StrictStr | None = None
