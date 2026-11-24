from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_tag_model import RDSTagModel
from .rds_user_auth_config import RDSUserAuthConfig


class RDSCreateDBProxyRequest(BaseModel):
    DBProxyName: StrictStr
    EngineFamily: Literal['MYSQL', 'POSTGRESQL', 'SQLSERVER']
    RoleArn: StrictStr
    VpcSubnetIds: list[StrictStr]
    DefaultAuthScheme: Literal['IAM_AUTH', 'NONE'] | None = None
    Auth: list[RDSUserAuthConfig] | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    RequireTLS: StrictBool | None = None
    IdleClientTimeout: StrictInt | None = None
    DebugLogging: StrictBool | None = None
    Tags: list[RDSTagModel] | None = None
    EndpointNetworkType: Literal['IPV4', 'IPV6', 'DUAL'] | None = None
    TargetConnectionNetworkType: Literal['IPV4', 'IPV6'] | None = None
