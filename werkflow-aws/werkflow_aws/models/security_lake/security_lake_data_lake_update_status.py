from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_lake_data_lake_update_exception import SecurityLakeDataLakeUpdateException


class SecurityLakeDataLakeUpdateStatus(BaseModel):
    exception: SecurityLakeDataLakeUpdateException | None = None
    requestId: StrictStr | None = None
    status: StrictStr | None = None
