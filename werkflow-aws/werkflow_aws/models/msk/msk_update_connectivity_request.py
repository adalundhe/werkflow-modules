from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_connectivity_info_model import MSKConnectivityInfoModel
from .msk_zookeeper_access import MSKZookeeperAccess


class MSKUpdateConnectivityRequest(BaseModel):
    ClusterArn: StrictStr
    CurrentVersion: StrictStr
    ConnectivityInfo: MSKConnectivityInfoModel | None = None
    ZookeeperAccess: MSKZookeeperAccess | None = None
