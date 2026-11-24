from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DirectoryServiceDescribeSettingsRequest(BaseModel):
    DirectoryId: StrictStr
    Status: Literal['Requested', 'Updating', 'Updated', 'Failed', 'Default'] | None = None
    NextToken: StrictStr | None = None
