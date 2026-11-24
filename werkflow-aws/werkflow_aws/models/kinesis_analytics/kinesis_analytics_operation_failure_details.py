from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_error_info import KinesisAnalyticsErrorInfo


class KinesisAnalyticsOperationFailureDetails(BaseModel):
    RollbackOperationId: StrictStr | None = None
    ErrorInfo: KinesisAnalyticsErrorInfo | None = None
