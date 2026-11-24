from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_user_auth_config_info import RDSUserAuthConfigInfo


class RDSDBProxy(BaseModel):
    DBProxyName: StrictStr | None = None
    DBProxyArn: StrictStr | None = None
    Status: StrictStr | None = None
    EngineFamily: StrictStr | None = None
    VpcId: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    VpcSubnetIds: list[StrictStr] | None = None
    DefaultAuthScheme: StrictStr | None = None
    Auth: list[RDSUserAuthConfigInfo] | None = None
    RoleArn: StrictStr | None = None
    Endpoint: StrictStr | None = None
    RequireTLS: StrictBool | None = None
    IdleClientTimeout: StrictInt | None = None
    DebugLogging: StrictBool | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    UpdatedDate: datetime.datetime | StrictStr | None = None
    EndpointNetworkType: StrictStr | None = None
    TargetConnectionNetworkType: StrictStr | None = None
