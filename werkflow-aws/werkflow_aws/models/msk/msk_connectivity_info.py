from pydantic import BaseModel
from .msk_connectivity_public_access import MSKConnectivityPublicAccess
from .msk_vpc_connectivity import MSKVpcConnectivity


class MSKConnectivityInfo(BaseModel):
    PublicAccess: MSKConnectivityPublicAccess
    VpcConnectivity: MSKVpcConnectivity