from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_query_info import ConfigServiceQueryInfo


class ConfigServiceSelectResourceConfigResponse(BaseModel):
    Results: list[StrictStr] | None = None
    QueryInfo: ConfigServiceQueryInfo | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
