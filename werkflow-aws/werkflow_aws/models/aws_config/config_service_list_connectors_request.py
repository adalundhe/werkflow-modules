from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_connector_filter import ConfigServiceConnectorFilter


class ConfigServiceListConnectorsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Filters: list[ConfigServiceConnectorFilter] | None = None
