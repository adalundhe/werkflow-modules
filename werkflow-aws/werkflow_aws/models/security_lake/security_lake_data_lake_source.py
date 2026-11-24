from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_lake_data_lake_source_status import SecurityLakeDataLakeSourceStatus


class SecurityLakeDataLakeSource(BaseModel):
    account: StrictStr | None = None
    eventClasses: list[StrictStr] | None = None
    sourceName: StrictStr | None = None
    sourceStatuses: list[SecurityLakeDataLakeSourceStatus] | None = None
