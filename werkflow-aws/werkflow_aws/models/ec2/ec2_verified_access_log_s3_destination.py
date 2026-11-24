from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_verified_access_log_delivery_status import EC2VerifiedAccessLogDeliveryStatus


class EC2VerifiedAccessLogS3Destination(BaseModel):
    Enabled: StrictBool | None = None
    DeliveryStatus: EC2VerifiedAccessLogDeliveryStatus | None = None
    BucketName: StrictStr | None = None
    Prefix: StrictStr | None = None
    BucketOwner: StrictStr | None = None
