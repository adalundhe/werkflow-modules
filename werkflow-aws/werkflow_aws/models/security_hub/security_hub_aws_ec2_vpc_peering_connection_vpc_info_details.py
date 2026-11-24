from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_vpc_info_cidr_block_set_details import SecurityHubVpcInfoCidrBlockSetDetails
from .security_hub_vpc_info_ipv6_cidr_block_set_details import SecurityHubVpcInfoIpv6CidrBlockSetDetails
from .security_hub_vpc_info_peering_options_details import SecurityHubVpcInfoPeeringOptionsDetails


class SecurityHubAwsEc2VpcPeeringConnectionVpcInfoDetails(BaseModel):
    CidrBlock: StrictStr | None = None
    CidrBlockSet: list[SecurityHubVpcInfoCidrBlockSetDetails] | None = None
    Ipv6CidrBlockSet: list[SecurityHubVpcInfoIpv6CidrBlockSetDetails] | None = None
    OwnerId: StrictStr | None = None
    PeeringOptions: SecurityHubVpcInfoPeeringOptionsDetails | None = None
    Region: StrictStr | None = None
    VpcId: StrictStr | None = None
