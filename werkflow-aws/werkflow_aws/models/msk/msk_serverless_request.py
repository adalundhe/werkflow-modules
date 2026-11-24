from __future__ import annotations
from pydantic import BaseModel
from .msk_serverless_client_authentication import MSKServerlessClientAuthentication
from .msk_vpc_config import MSKVpcConfig


class MSKServerlessRequest(BaseModel):
    VpcConfigs: list[MSKVpcConfig]
    ClientAuthentication: MSKServerlessClientAuthentication | None = None
