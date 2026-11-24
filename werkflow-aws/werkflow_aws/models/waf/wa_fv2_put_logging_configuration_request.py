from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_logging_configuration import WAFv2LoggingConfiguration


class WAFv2PutLoggingConfigurationRequest(BaseModel):
    LoggingConfiguration: WAFv2LoggingConfiguration
