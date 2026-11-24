from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class EC2DescribeAccountAttributesRequest(BaseModel):
    DryRun: StrictBool | None = None
    AttributeNames: list[Literal['supported-platforms', 'default-vpc']] | None = None
