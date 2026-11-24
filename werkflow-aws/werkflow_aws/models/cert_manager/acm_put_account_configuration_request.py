from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .acm_expiry_events_configuration import ACMExpiryEventsConfiguration


class ACMPutAccountConfigurationRequest(BaseModel):
    IdempotencyToken: StrictStr
    ExpiryEvents: ACMExpiryEventsConfiguration | None = None
