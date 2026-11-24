from __future__ import annotations
from pydantic import BaseModel
from .security_hub_ai_details import SecurityHubAIDetails


class SecurityHubResourceInfo(BaseModel):
    AIDetails: SecurityHubAIDetails | None = None
