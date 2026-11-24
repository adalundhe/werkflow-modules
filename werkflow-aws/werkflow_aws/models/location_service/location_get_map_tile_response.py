from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class LocationGetMapTileResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Blob: StrictBytes | Any | None = None
    ContentType: StrictStr | None = None
    CacheControl: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
