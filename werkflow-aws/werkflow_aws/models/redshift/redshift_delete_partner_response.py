from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class RedshiftDeletePartnerResponse(BaseModel):
    DatabaseName: StrictStr | None = None
    PartnerName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
