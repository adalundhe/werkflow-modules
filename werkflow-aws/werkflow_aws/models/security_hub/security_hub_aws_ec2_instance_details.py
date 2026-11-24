from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_ec2_instance_metadata_options import SecurityHubAwsEc2InstanceMetadataOptions
from .security_hub_aws_ec2_instance_monitoring_details import SecurityHubAwsEc2InstanceMonitoringDetails
from .security_hub_aws_ec2_instance_network_interfaces_details import SecurityHubAwsEc2InstanceNetworkInterfacesDetails


class SecurityHubAwsEc2InstanceDetails(BaseModel):
    Type: StrictStr | None = None
    ImageId: StrictStr | None = None
    IpV4Addresses: list[StrictStr] | None = None
    IpV6Addresses: list[StrictStr] | None = None
    KeyName: StrictStr | None = None
    IamInstanceProfileArn: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    LaunchedAt: StrictStr | None = None
    NetworkInterfaces: list[SecurityHubAwsEc2InstanceNetworkInterfacesDetails] | None = None
    VirtualizationType: StrictStr | None = None
    MetadataOptions: SecurityHubAwsEc2InstanceMetadataOptions | None = None
    Monitoring: SecurityHubAwsEc2InstanceMonitoringDetails | None = None
