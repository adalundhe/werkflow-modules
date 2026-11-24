from __future__ import annotations
from pydantic import BaseModel
from .security_hub_sequence import SecurityHubSequence


class SecurityHubDetection(BaseModel):
    Sequence: SecurityHubSequence | None = None
