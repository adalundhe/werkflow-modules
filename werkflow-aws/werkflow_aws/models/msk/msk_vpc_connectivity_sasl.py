from __future__ import annotations
from pydantic import BaseModel
from .msk_vpc_connectivity_iam import MSKVpcConnectivityIam
from .msk_vpc_connectivity_scram import MSKVpcConnectivityScram


class MSKVpcConnectivitySasl(BaseModel):
    Scram: MSKVpcConnectivityScram | None = None
    Iam: MSKVpcConnectivityIam | None = None
