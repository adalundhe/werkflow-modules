from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ses_suppressed_destination import SESSuppressedDestination


class SESGetSuppressedDestinationResponse(BaseModel):
    SuppressedDestination: SESSuppressedDestination | None = None
    ResponseMetadata: dict[str, Any] | None = None
