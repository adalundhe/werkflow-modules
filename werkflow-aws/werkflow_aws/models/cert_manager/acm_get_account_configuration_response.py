from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .acm_expiry_events_configuration import ACMExpiryEventsConfiguration


class ACMGetAccountConfigurationResponse(BaseModel):
    ExpiryEvents: ACMExpiryEventsConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
