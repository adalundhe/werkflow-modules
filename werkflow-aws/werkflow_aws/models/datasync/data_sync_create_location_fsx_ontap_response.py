from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DataSyncCreateLocationFsxOntapResponse(BaseModel):
    LocationArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
