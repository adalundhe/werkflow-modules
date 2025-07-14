from pydantic import BaseModel
from .msk_vpc_client_authentication import MSKVPCClientAuthentication


class MSKVpcConnectivity(BaseModel):
    ClientAuthentication: MSKVPCClientAuthentication
