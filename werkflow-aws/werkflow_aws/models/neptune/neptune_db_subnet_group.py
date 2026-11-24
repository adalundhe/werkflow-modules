from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_subnet import NeptuneSubnet


class NeptuneDBSubnetGroup(BaseModel):
    DBSubnetGroupName: StrictStr | None = None
    DBSubnetGroupDescription: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetGroupStatus: StrictStr | None = None
    Subnets: list[NeptuneSubnet] | None = None
    DBSubnetGroupArn: StrictStr | None = None
    SupportedNetworkTypes: list[StrictStr] | None = None
