from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_delivery_destination_configuration import CloudWatchLogsDeliveryDestinationConfiguration


class CloudWatchLogsPutDeliveryDestinationRequest(BaseModel):
    name: StrictStr
    outputFormat: Literal['json', 'plain', 'w3c', 'raw', 'parquet'] | None = None
    deliveryDestinationConfiguration: CloudWatchLogsDeliveryDestinationConfiguration | None = None
    deliveryDestinationType: Literal['S3', 'CWL', 'FH', 'XRAY'] | None = None
    roleArn: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
