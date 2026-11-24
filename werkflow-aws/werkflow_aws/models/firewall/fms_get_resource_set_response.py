from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_resource_set import FMSResourceSet


class FMSGetResourceSetResponse(BaseModel):
    ResourceSet: FMSResourceSet | None = None
    ResourceSetArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
