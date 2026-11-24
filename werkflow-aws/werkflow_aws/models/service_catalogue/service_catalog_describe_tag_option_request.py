from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDescribeTagOptionRequest(BaseModel):
    Id: StrictStr
