from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_user_auth_config import RDSUserAuthConfig


class RDSModifyDBProxyRequest(BaseModel):
    DBProxyName: StrictStr
    NewDBProxyName: StrictStr | None = None
    DefaultAuthScheme: Literal['IAM_AUTH', 'NONE'] | None = None
    Auth: list[RDSUserAuthConfig] | None = None
    RequireTLS: StrictBool | None = None
    IdleClientTimeout: StrictInt | None = None
    DebugLogging: StrictBool | None = None
    RoleArn: StrictStr | None = None
    SecurityGroups: list[StrictStr] | None = None
