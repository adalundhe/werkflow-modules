from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class EC2ModifyManagedResourceVisibilityRequest(BaseModel):
    DefaultVisibility: Literal['hidden', 'visible']
    DryRun: StrictBool | None = None
