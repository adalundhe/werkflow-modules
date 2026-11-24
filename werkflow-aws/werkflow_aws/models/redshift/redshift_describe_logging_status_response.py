from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .redshift_s3_table_publish_status import RedshiftS3TablePublishStatus


class RedshiftDescribeLoggingStatusResponse(BaseModel):
    LoggingEnabled: StrictBool | None = None
    BucketName: StrictStr | None = None
    S3KeyPrefix: StrictStr | None = None
    LastSuccessfulDeliveryTime: datetime.datetime | StrictStr | None = None
    LastFailureTime: datetime.datetime | StrictStr | None = None
    LastFailureMessage: StrictStr | None = None
    LogDestinationType: StrictStr | None = None
    LogExports: list[StrictStr] | None = None
    S3Tables: RedshiftS3TablePublishStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
