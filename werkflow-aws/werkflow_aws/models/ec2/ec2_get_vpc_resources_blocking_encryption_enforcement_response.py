from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_vpc_encryption_non_compliant_resource import EC2VpcEncryptionNonCompliantResource


class EC2GetVpcResourcesBlockingEncryptionEnforcementResponse(BaseModel):
    NonCompliantResources: list[EC2VpcEncryptionNonCompliantResource] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
