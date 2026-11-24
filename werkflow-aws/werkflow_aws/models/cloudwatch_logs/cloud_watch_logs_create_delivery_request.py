from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_s3_delivery_configuration import CloudWatchLogsS3DeliveryConfiguration


class CloudWatchLogsCreateDeliveryRequest(BaseModel):
    deliverySourceName: StrictStr
    deliveryDestinationArn: StrictStr
    recordFields: list[StrictStr] | None = None
    fieldDelimiter: StrictStr | None = None
    s3DeliveryConfiguration: CloudWatchLogsS3DeliveryConfiguration | None = None
    tags: dict[StrictStr, StrictStr] | None = None
