from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDirectoryVpcSettings(BaseModel):
    VpcId: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
