from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag import EC2Tag


class EC2DeleteTagsRequest(BaseModel):
    Resources: list[StrictStr]
    Tags: list[EC2Tag] | None = None
    DryRun: StrictBool | None = None
