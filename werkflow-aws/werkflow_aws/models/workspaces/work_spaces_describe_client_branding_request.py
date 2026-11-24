from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDescribeClientBrandingRequest(BaseModel):
    ResourceId: StrictStr
