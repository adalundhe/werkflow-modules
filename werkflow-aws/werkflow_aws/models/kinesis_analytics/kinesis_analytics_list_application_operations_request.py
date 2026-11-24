from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsListApplicationOperationsRequest(BaseModel):
    ApplicationName: StrictStr
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
    Operation: StrictStr | None = None
    OperationStatus: Literal['IN_PROGRESS', 'CANCELLED', 'SUCCESSFUL', 'FAILED'] | None = None
