from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_unsuccessful_item import EC2UnsuccessfulItem


class EC2ModifyHostsResponse(BaseModel):
    Successful: list[StrictStr] | None = None
    Unsuccessful: list[EC2UnsuccessfulItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
