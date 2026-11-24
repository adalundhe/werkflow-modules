from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_tag_description import EC2TagDescription


class EC2DescribeTagsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Tags: list[EC2TagDescription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
