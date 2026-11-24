from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SecurityHubCreateTicketV2Request(BaseModel):
    ConnectorId: StrictStr
    FindingMetadataUid: StrictStr
    ClientToken: StrictStr | None = None
    Mode: Literal['DRYRUN'] | None = None
