from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeliverySource(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    resourceArns: list[StrictStr] | None = None
    service: StrictStr | None = None
    logType: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    deliverySourceConfiguration: dict[StrictStr, StrictStr] | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
