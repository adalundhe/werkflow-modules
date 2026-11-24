from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .support_communication import SupportCommunication


class SupportDescribeCommunicationsResponse(BaseModel):
    communications: list[SupportCommunication] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
