from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_conformance_pack_detail import ConfigServiceConformancePackDetail


class ConfigServiceDescribeConformancePacksResponse(BaseModel):
    ConformancePackDetails: list[ConfigServiceConformancePackDetail] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
