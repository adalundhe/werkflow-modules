from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DirectoryServiceDescribeUpdateDirectoryRequest(BaseModel):
    DirectoryId: StrictStr
    UpdateType: Literal['OS', 'NETWORK', 'SIZE']
    RegionName: StrictStr | None = None
    NextToken: StrictStr | None = None
