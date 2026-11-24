from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_verified_access_endpoint_cidr_options import EC2VerifiedAccessEndpointCidrOptions
from .ec2_verified_access_endpoint_eni_options import EC2VerifiedAccessEndpointEniOptions
from .ec2_verified_access_endpoint_load_balancer_options import EC2VerifiedAccessEndpointLoadBalancerOptions
from .ec2_verified_access_endpoint_rds_options import EC2VerifiedAccessEndpointRdsOptions
from .ec2_verified_access_endpoint_status import EC2VerifiedAccessEndpointStatus
from .ec2_verified_access_sse_specification_response import EC2VerifiedAccessSseSpecificationResponse


class EC2VerifiedAccessEndpoint(BaseModel):
    VerifiedAccessInstanceId: StrictStr | None = None
    VerifiedAccessGroupId: StrictStr | None = None
    VerifiedAccessEndpointId: StrictStr | None = None
    ApplicationDomain: StrictStr | None = None
    EndpointType: StrictStr | None = None
    AttachmentType: StrictStr | None = None
    DomainCertificateArn: StrictStr | None = None
    EndpointDomain: StrictStr | None = None
    DeviceValidationDomain: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    LoadBalancerOptions: EC2VerifiedAccessEndpointLoadBalancerOptions | None = None
    NetworkInterfaceOptions: EC2VerifiedAccessEndpointEniOptions | None = None
    Status: EC2VerifiedAccessEndpointStatus | None = None
    Description: StrictStr | None = None
    CreationTime: StrictStr | None = None
    LastUpdatedTime: StrictStr | None = None
    DeletionTime: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    SseSpecification: EC2VerifiedAccessSseSpecificationResponse | None = None
    RdsOptions: EC2VerifiedAccessEndpointRdsOptions | None = None
    CidrOptions: EC2VerifiedAccessEndpointCidrOptions | None = None
