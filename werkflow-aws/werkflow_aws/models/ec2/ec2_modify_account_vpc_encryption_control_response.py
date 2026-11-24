from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_account_vpc_encryption_control import EC2AccountVpcEncryptionControl


class EC2ModifyAccountVpcEncryptionControlResponse(BaseModel):
    AccountVpcEncryptionControl: EC2AccountVpcEncryptionControl | None = None
    ResponseMetadata: dict[str, Any] | None = None
