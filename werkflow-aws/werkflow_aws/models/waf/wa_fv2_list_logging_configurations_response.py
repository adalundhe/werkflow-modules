from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_logging_configuration import WAFv2LoggingConfiguration


class WAFv2ListLoggingConfigurationsResponse(BaseModel):
    LoggingConfigurations: list[WAFv2LoggingConfiguration] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
