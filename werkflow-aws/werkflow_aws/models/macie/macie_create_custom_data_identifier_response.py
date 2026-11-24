from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MacieCreateCustomDataIdentifierResponse(BaseModel):
    customDataIdentifierId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
