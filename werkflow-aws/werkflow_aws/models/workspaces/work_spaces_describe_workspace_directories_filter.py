from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WorkSpacesDescribeWorkspaceDirectoriesFilter(BaseModel):
    Name: Literal['USER_IDENTITY_TYPE', 'WORKSPACE_TYPE']
    Values: list[StrictStr]
