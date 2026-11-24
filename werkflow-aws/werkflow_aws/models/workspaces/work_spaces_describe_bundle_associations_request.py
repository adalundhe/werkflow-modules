from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WorkSpacesDescribeBundleAssociationsRequest(BaseModel):
    BundleId: StrictStr
    AssociatedResourceTypes: list[Literal['APPLICATION']]
