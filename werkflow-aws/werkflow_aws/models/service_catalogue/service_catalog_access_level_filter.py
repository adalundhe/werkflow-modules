from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ServiceCatalogAccessLevelFilter(BaseModel):
    Key: Literal['Account', 'Role', 'User'] | None = None
    Value: StrictStr | None = None
