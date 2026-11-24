from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2VpcClassicLink(BaseModel):
    ClassicLinkEnabled: StrictBool | None = None
    Tags: list[EC2TagModel] | None = None
    VpcId: StrictStr | None = None
