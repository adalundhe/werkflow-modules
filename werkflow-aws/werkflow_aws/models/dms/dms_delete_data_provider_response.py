from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_data_provider import DMSDataProvider


class DMSDeleteDataProviderResponse(BaseModel):
    DataProvider: DMSDataProvider | None = None
    ResponseMetadata: dict[str, Any] | None = None
