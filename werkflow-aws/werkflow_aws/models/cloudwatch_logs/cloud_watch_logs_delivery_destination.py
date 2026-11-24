from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_delivery_destination_configuration import CloudWatchLogsDeliveryDestinationConfiguration


class CloudWatchLogsDeliveryDestination(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    deliveryDestinationType: StrictStr | None = None
    outputFormat: StrictStr | None = None
    deliveryDestinationConfiguration: CloudWatchLogsDeliveryDestinationConfiguration | None = None
    roleArn: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
