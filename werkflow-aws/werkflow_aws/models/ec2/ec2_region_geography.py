from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2RegionGeography(BaseModel):
    Name: StrictStr | None = None
