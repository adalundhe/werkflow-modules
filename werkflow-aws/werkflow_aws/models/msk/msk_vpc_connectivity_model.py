from __future__ import annotations
from pydantic import BaseModel
from .msk_vpc_connectivity_client_authentication import MSKVpcConnectivityClientAuthentication


class MSKVpcConnectivityModel(BaseModel):
    ClientAuthentication: MSKVpcConnectivityClientAuthentication | None = None
