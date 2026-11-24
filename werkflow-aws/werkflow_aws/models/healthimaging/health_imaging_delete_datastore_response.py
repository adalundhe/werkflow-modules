from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class HealthImagingDeleteDatastoreResponse(BaseModel):
    datastoreId: StrictStr | None = None
    datastoreStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
