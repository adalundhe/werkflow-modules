from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class HealthImagingCreateDatastoreResponse(BaseModel):
    datastoreId: StrictStr | None = None
    datastoreStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
