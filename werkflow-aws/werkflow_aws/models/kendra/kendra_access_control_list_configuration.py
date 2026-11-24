from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraAccessControlListConfiguration(BaseModel):
    KeyPath: StrictStr | None = None
