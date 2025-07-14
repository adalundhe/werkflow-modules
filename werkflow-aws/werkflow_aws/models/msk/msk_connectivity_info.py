from pydantic import BaseModel, StrictStr
from .msk_connectivity_public_access import MSKConnectivityPublicAccess
from .msk_vpc_connectivity import MSKVpcConnectivity


class MSKConnectivityInfo(BaseModel):
    PublicAccess: MSKConnectivityPublicAccess
    VpcConnectivity: MSKVpcConnectivity
    ZoneIds: list[StrictStr]