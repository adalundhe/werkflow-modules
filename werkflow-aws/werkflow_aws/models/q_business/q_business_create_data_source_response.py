from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class QBusinessCreateDataSourceResponse(BaseModel):
    dataSourceId: StrictStr | None = None
    dataSourceArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
