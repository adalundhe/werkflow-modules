from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_storage import EC2Storage


class EC2BundleInstanceRequest(BaseModel):
    InstanceId: StrictStr
    Storage: EC2Storage
    DryRun: StrictBool | None = None
