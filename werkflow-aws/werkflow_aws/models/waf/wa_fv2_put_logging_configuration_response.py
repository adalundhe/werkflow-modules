from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .wa_fv2_logging_configuration import WAFv2LoggingConfiguration


class WAFv2PutLoggingConfigurationResponse(BaseModel):
    LoggingConfiguration: WAFv2LoggingConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
