from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LightsailGetActiveNamesResponse(BaseModel):
    activeNames: list[StrictStr] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
