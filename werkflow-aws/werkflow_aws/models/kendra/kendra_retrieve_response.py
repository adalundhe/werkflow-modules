from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_retrieve_result_item import KendraRetrieveResultItem


class KendraRetrieveResponse(BaseModel):
    QueryId: StrictStr | None = None
    ResultItems: list[KendraRetrieveResultItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
