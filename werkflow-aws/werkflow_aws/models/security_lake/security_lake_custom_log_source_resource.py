from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_lake_custom_log_source_attributes import SecurityLakeCustomLogSourceAttributes
from .security_lake_custom_log_source_provider import SecurityLakeCustomLogSourceProvider


class SecurityLakeCustomLogSourceResource(BaseModel):
    attributes: SecurityLakeCustomLogSourceAttributes | None = None
    provider: SecurityLakeCustomLogSourceProvider | None = None
    sourceName: StrictStr | None = None
    sourceVersion: StrictStr | None = None
