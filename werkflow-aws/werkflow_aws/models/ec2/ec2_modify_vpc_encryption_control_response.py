from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_vpc_encryption_control import EC2VpcEncryptionControl


class EC2ModifyVpcEncryptionControlResponse(BaseModel):
    VpcEncryptionControl: EC2VpcEncryptionControl | None = None
    ResponseMetadata: dict[str, Any] | None = None
