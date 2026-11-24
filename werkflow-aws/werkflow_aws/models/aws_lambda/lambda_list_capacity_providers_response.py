from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lambda_capacity_provider import LambdaCapacityProvider


class LambdaListCapacityProvidersResponse(BaseModel):
    CapacityProviders: list[LambdaCapacityProvider] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
