from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_public_access import MSKPublicAccess
from .msk_vpc_connectivity_model import MSKVpcConnectivityModel


class MSKConnectivityInfoModel(BaseModel):
    PublicAccess: MSKPublicAccess | None = None
    VpcConnectivity: MSKVpcConnectivityModel | None = None
    NetworkType: StrictStr | None = None
