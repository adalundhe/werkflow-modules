from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_connector_summary import ConfigServiceConnectorSummary


class ConfigServiceListConnectorsResponse(BaseModel):
    ConnectorSummaries: list[ConfigServiceConnectorSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
