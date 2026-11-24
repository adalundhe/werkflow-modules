from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GluePutFormTypeResponse(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Schema: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
