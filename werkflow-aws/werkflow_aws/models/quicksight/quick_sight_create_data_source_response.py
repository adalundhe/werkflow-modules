from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightCreateDataSourceResponse(BaseModel):
    Arn: StrictStr | None = None
    DataSourceId: StrictStr | None = None
    CreationStatus: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
