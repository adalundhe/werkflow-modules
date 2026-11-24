from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecs_capacity_provider import ECSCapacityProvider
from .ecs_failure import ECSFailure


class ECSDescribeCapacityProvidersResponse(BaseModel):
    capacityProviders: list[ECSCapacityProvider] | None = None
    failures: list[ECSFailure] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
