from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .efs_access_point_description import EFSAccessPointDescription


class EFSDescribeAccessPointsResponse(BaseModel):
    AccessPoints: list[EFSAccessPointDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
