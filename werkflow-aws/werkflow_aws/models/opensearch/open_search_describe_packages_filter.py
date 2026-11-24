from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchDescribePackagesFilter(BaseModel):
    Name: Literal['PackageID', 'PackageName', 'PackageStatus', 'PackageType', 'EngineVersion', 'PackageOwner'] | None = None
    Value: list[StrictStr] | None = None
