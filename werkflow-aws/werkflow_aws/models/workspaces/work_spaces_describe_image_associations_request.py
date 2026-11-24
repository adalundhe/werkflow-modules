from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WorkSpacesDescribeImageAssociationsRequest(BaseModel):
    ImageId: StrictStr
    AssociatedResourceTypes: list[Literal['APPLICATION']]
