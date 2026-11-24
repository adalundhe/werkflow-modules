from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_list_keys_response_entry import LocationListKeysResponseEntry


class LocationListKeysResponse(BaseModel):
    Entries: list[LocationListKeysResponseEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
