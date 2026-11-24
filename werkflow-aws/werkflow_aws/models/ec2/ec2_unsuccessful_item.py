from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_unsuccessful_item_error import EC2UnsuccessfulItemError


class EC2UnsuccessfulItem(BaseModel):
    Error: EC2UnsuccessfulItemError | None = None
    ResourceId: StrictStr | None = None
