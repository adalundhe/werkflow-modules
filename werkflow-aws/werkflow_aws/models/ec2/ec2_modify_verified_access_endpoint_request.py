from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_modify_verified_access_endpoint_cidr_options import EC2ModifyVerifiedAccessEndpointCidrOptions
from .ec2_modify_verified_access_endpoint_eni_options import EC2ModifyVerifiedAccessEndpointEniOptions
from .ec2_modify_verified_access_endpoint_load_balancer_options import EC2ModifyVerifiedAccessEndpointLoadBalancerOptions
from .ec2_modify_verified_access_endpoint_rds_options import EC2ModifyVerifiedAccessEndpointRdsOptions


class EC2ModifyVerifiedAccessEndpointRequest(BaseModel):
    VerifiedAccessEndpointId: StrictStr
    VerifiedAccessGroupId: StrictStr | None = None
    LoadBalancerOptions: EC2ModifyVerifiedAccessEndpointLoadBalancerOptions | None = None
    NetworkInterfaceOptions: EC2ModifyVerifiedAccessEndpointEniOptions | None = None
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    RdsOptions: EC2ModifyVerifiedAccessEndpointRdsOptions | None = None
    CidrOptions: EC2ModifyVerifiedAccessEndpointCidrOptions | None = None
