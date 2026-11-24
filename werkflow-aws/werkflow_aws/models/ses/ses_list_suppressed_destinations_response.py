from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_suppressed_destination_summary import SESSuppressedDestinationSummary


class SESListSuppressedDestinationsResponse(BaseModel):
    SuppressedDestinationSummaries: list[SESSuppressedDestinationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
