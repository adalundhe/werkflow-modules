from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_failed_item import FMSFailedItem


class FMSBatchAssociateResourceResponse(BaseModel):
    ResourceSetIdentifier: StrictStr | None = None
    FailedItems: list[FMSFailedItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
