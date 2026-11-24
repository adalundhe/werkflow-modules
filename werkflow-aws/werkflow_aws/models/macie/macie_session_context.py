from __future__ import annotations
from pydantic import BaseModel
from .macie_session_context_attributes import MacieSessionContextAttributes
from .macie_session_issuer import MacieSessionIssuer


class MacieSessionContext(BaseModel):
    attributes: MacieSessionContextAttributes | None = None
    sessionIssuer: MacieSessionIssuer | None = None
