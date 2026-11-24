from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2InstanceEventWindowDisassociationRequest(BaseModel):
    InstanceIds: list[StrictStr] | None = None
    InstanceTags: list[EC2TagModel] | None = None
    DedicatedHostIds: list[StrictStr] | None = None
