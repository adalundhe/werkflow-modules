from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_search_availability_options_status import CloudSearchAvailabilityOptionsStatus


class CloudSearchUpdateAvailabilityOptionsResponse(BaseModel):
    AvailabilityOptions: CloudSearchAvailabilityOptionsStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
