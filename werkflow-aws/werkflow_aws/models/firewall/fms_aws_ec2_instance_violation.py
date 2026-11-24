from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_aws_ec2_network_interface_violation import FMSAwsEc2NetworkInterfaceViolation


class FMSAwsEc2InstanceViolation(BaseModel):
    ViolationTarget: StrictStr | None = None
    AwsEc2NetworkInterfaceViolations: list[FMSAwsEc2NetworkInterfaceViolation] | None = None
