from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_vpc_encryption_control import EC2VpcEncryptionControl


class EC2DescribeVpcEncryptionControlsResponse(BaseModel):
    VpcEncryptionControls: list[EC2VpcEncryptionControl] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
