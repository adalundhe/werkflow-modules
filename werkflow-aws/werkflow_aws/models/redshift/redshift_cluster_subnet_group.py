from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_subnet import RedshiftSubnet
from .redshift_tag import RedshiftTag


class RedshiftClusterSubnetGroup(BaseModel):
    ClusterSubnetGroupName: StrictStr | None = None
    Description: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetGroupStatus: StrictStr | None = None
    Subnets: list[RedshiftSubnet] | None = None
    Tags: list[RedshiftTag] | None = None
    SupportedClusterIpAddressTypes: list[StrictStr] | None = None
