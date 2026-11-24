from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_aggregate_resource_identifier import ConfigServiceAggregateResourceIdentifier


class ConfigServiceListAggregateDiscoveredResourcesResponse(BaseModel):
    ResourceIdentifiers: list[ConfigServiceAggregateResourceIdentifier] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
