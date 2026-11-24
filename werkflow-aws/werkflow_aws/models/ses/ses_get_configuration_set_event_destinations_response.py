from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ses_event_destination import SESEventDestination


class SESGetConfigurationSetEventDestinationsResponse(BaseModel):
    EventDestinations: list[SESEventDestination] | None = None
    ResponseMetadata: dict[str, Any] | None = None
