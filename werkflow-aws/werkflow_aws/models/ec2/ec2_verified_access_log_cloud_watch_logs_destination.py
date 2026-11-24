from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_verified_access_log_delivery_status import EC2VerifiedAccessLogDeliveryStatus


class EC2VerifiedAccessLogCloudWatchLogsDestination(BaseModel):
    Enabled: StrictBool | None = None
    DeliveryStatus: EC2VerifiedAccessLogDeliveryStatus | None = None
    LogGroup: StrictStr | None = None
