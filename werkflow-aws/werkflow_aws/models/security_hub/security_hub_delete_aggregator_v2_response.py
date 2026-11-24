from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class SecurityHubDeleteAggregatorV2Response(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
