from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_data_provider import DMSDataProvider


class DMSDescribeDataProvidersResponse(BaseModel):
    Marker: StrictStr | None = None
    DataProviders: list[DMSDataProvider] | None = None
    ResponseMetadata: dict[str, Any] | None = None
