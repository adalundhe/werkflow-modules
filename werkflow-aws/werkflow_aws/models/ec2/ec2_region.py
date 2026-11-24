from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_region_geography import EC2RegionGeography


class EC2Region(BaseModel):
    OptInStatus: StrictStr | None = None
    Geography: list[EC2RegionGeography] | None = None
    RegionName: StrictStr | None = None
    Endpoint: StrictStr | None = None
