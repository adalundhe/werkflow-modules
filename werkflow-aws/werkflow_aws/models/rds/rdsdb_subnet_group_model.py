from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_subnet_model import RDSSubnetModel


class RDSDBSubnetGroupModel(BaseModel):
    DBSubnetGroupName: StrictStr | None = None
    DBSubnetGroupDescription: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetGroupStatus: StrictStr | None = None
    Subnets: list[RDSSubnetModel] | None = None
    DBSubnetGroupArn: StrictStr | None = None
    SupportedNetworkTypes: list[StrictStr] | None = None
