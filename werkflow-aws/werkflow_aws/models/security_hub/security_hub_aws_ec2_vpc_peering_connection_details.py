from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_ec2_vpc_peering_connection_status_details import SecurityHubAwsEc2VpcPeeringConnectionStatusDetails
from .security_hub_aws_ec2_vpc_peering_connection_vpc_info_details import SecurityHubAwsEc2VpcPeeringConnectionVpcInfoDetails


class SecurityHubAwsEc2VpcPeeringConnectionDetails(BaseModel):
    AccepterVpcInfo: SecurityHubAwsEc2VpcPeeringConnectionVpcInfoDetails | None = None
    ExpirationTime: StrictStr | None = None
    RequesterVpcInfo: SecurityHubAwsEc2VpcPeeringConnectionVpcInfoDetails | None = None
    Status: SecurityHubAwsEc2VpcPeeringConnectionStatusDetails | None = None
    VpcPeeringConnectionId: StrictStr | None = None
