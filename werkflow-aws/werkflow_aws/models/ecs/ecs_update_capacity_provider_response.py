from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_capacity_provider import ECSCapacityProvider


class ECSUpdateCapacityProviderResponse(BaseModel):
    capacityProvider: ECSCapacityProvider | None = None
    ResponseMetadata: dict[str, Any] | None = None
