from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .cloud_search_option_status import CloudSearchOptionStatus


class CloudSearchAvailabilityOptionsStatus(BaseModel):
    Options: StrictBool | None = None
    Status: CloudSearchOptionStatus | None = None
