from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .open_search_cancelled_change_property import OpenSearchCancelledChangeProperty


class OpenSearchCancelDomainConfigChangeResponse(BaseModel):
    CancelledChangeIds: list[StrictStr] | None = None
    CancelledChangeProperties: list[OpenSearchCancelledChangeProperty] | None = None
    DryRun: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
