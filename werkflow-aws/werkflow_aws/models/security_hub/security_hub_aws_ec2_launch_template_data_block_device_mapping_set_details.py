from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_ec2_launch_template_data_block_device_mapping_set_ebs_details import SecurityHubAwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails


class SecurityHubAwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails(BaseModel):
    DeviceName: StrictStr | None = None
    Ebs: SecurityHubAwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails | None = None
    NoDevice: StrictStr | None = None
    VirtualName: StrictStr | None = None
