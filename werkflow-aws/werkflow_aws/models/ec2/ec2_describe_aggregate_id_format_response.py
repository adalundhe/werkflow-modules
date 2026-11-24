from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool
from .ec2_id_format import EC2IdFormat


class EC2DescribeAggregateIdFormatResponse(BaseModel):
    UseLongIdsAggregated: StrictBool | None = None
    Statuses: list[EC2IdFormat] | None = None
    ResponseMetadata: dict[str, Any] | None = None
