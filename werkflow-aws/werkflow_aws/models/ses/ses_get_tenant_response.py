from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ses_tenant import SESTenant


class SESGetTenantResponse(BaseModel):
    Tenant: SESTenant | None = None
    ResponseMetadata: dict[str, Any] | None = None
