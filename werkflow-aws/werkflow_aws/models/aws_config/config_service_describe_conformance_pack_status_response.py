from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_conformance_pack_status_detail import ConfigServiceConformancePackStatusDetail


class ConfigServiceDescribeConformancePackStatusResponse(BaseModel):
    ConformancePackStatusDetails: list[ConfigServiceConformancePackStatusDetail] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
