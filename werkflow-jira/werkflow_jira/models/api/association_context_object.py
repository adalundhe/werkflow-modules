from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AssociationContextObject(BaseModel):
    identifier: dict[StrictStr, Any] | None = None
    type: StrictStr | None = None
