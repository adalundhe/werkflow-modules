from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_network_acl import EC2NetworkAcl


class EC2CreateNetworkAclResponse(BaseModel):
    NetworkAcl: EC2NetworkAcl | None = None
    ClientToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
