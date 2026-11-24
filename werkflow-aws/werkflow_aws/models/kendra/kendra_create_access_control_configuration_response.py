from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class KendraCreateAccessControlConfigurationResponse(BaseModel):
    Id: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
