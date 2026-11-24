from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_group_identifier_model import EC2GroupIdentifierModel
from .ec2_tag_model import EC2TagModel


class EC2ClassicLinkInstance(BaseModel):
    Groups: list[EC2GroupIdentifierModel] | None = None
    InstanceId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    VpcId: StrictStr | None = None
