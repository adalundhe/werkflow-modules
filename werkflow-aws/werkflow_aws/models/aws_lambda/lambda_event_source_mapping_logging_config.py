from __future__ import annotations
from pydantic import BaseModel
from .lambda_event_source_mapping_system_log_level import LambdaEventSourceMappingSystemLogLevel


class LambdaEventSourceMappingLoggingConfig(BaseModel):
    SystemLogLevel: LambdaEventSourceMappingSystemLogLevel | None = None
