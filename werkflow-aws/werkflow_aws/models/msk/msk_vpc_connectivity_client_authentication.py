from __future__ import annotations
from pydantic import BaseModel
from .msk_vpc_connectivity_sasl import MSKVpcConnectivitySasl
from .msk_vpc_connectivity_tls import MSKVpcConnectivityTls


class MSKVpcConnectivityClientAuthentication(BaseModel):
    Sasl: MSKVpcConnectivitySasl | None = None
    Tls: MSKVpcConnectivityTls | None = None
