from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_mac_modification_task import EC2MacModificationTask


class EC2CreateMacSystemIntegrityProtectionModificationTaskResponse(BaseModel):
    MacModificationTask: EC2MacModificationTask | None = None
    ResponseMetadata: dict[str, Any] | None = None
