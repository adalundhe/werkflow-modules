from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_connection_pool_configuration_info import RDSConnectionPoolConfigurationInfo


class RDSDBProxyTargetGroup(BaseModel):
    DBProxyName: StrictStr | None = None
    TargetGroupName: StrictStr | None = None
    TargetGroupArn: StrictStr | None = None
    IsDefault: StrictBool | None = None
    Status: StrictStr | None = None
    ConnectionPoolConfig: RDSConnectionPoolConfigurationInfo | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    UpdatedDate: datetime.datetime | StrictStr | None = None
