from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_lake_custom_log_source_configuration import SecurityLakeCustomLogSourceConfiguration


class SecurityLakeCreateCustomLogSourceRequest(BaseModel):
    configuration: SecurityLakeCustomLogSourceConfiguration
    sourceName: StrictStr
    eventClasses: list[StrictStr] | None = None
    sourceVersion: StrictStr | None = None
