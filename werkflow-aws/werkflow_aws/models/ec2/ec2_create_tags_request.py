from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag import EC2Tag


class EC2CreateTagsRequest(BaseModel):
    Resources: list[StrictStr]
    Tags: list[EC2Tag]
    DryRun: StrictBool | None = None
