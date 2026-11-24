from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_error_info import QuickSightErrorInfo
from .quick_sight_queue_info import QuickSightQueueInfo
from .quick_sight_row_info import QuickSightRowInfo


class QuickSightIngestion(BaseModel):
    Arn: StrictStr | None = None
    IngestionId: StrictStr | None = None
    IngestionStatus: StrictStr | None = None
    ErrorInfo: QuickSightErrorInfo | None = None
    RowInfo: QuickSightRowInfo | None = None
    QueueInfo: QuickSightQueueInfo | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    IngestionTimeInSeconds: StrictInt | None = None
    IngestionSizeInBytes: StrictInt | None = None
    RequestSource: StrictStr | None = None
    RequestType: StrictStr | None = None
