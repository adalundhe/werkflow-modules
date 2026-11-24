from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .support_communication import SupportCommunication


class SupportRecentCaseCommunications(BaseModel):
    communications: list[SupportCommunication] | None = None
    nextToken: StrictStr | None = None
