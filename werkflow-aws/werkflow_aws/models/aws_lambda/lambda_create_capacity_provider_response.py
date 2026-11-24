from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lambda_capacity_provider import LambdaCapacityProvider


class LambdaCreateCapacityProviderResponse(BaseModel):
    CapacityProvider: LambdaCapacityProvider | None = None
    ResponseMetadata: dict[str, Any] | None = None
