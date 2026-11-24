from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EC2LoadPermissionRequest(BaseModel):
    Group: Literal['all'] | None = None
    UserId: StrictStr | None = None
