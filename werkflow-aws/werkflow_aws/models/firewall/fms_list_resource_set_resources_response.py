from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_resource import FMSResource


class FMSListResourceSetResourcesResponse(BaseModel):
    Items: list[FMSResource] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
