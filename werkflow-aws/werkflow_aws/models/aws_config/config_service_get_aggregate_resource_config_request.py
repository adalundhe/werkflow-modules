from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_aggregate_resource_identifier import ConfigServiceAggregateResourceIdentifier


class ConfigServiceGetAggregateResourceConfigRequest(BaseModel):
    ConfigurationAggregatorName: StrictStr
    ResourceIdentifier: ConfigServiceAggregateResourceIdentifier
