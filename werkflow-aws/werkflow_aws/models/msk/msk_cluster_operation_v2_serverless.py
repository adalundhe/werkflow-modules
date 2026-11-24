from __future__ import annotations
from pydantic import BaseModel
from .msk_serverless_connectivity_info import MSKServerlessConnectivityInfo
from .msk_vpc_connection_info_serverless import MSKVpcConnectionInfoServerless


class MSKClusterOperationV2Serverless(BaseModel):
    SourceClusterInfo: MSKServerlessConnectivityInfo | None = None
    TargetClusterInfo: MSKServerlessConnectivityInfo | None = None
    VpcConnectionInfo: MSKVpcConnectionInfoServerless | None = None
