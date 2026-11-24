from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_application_version_change_details import KinesisAnalyticsApplicationVersionChangeDetails
from .kinesis_analytics_operation_failure_details import KinesisAnalyticsOperationFailureDetails


class KinesisAnalyticsApplicationOperationInfoDetails(BaseModel):
    Operation: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    OperationStatus: StrictStr | None = None
    ApplicationVersionChangeDetails: KinesisAnalyticsApplicationVersionChangeDetails | None = None
    OperationFailureDetails: KinesisAnalyticsOperationFailureDetails | None = None
