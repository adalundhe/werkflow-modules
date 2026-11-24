from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2VerifiedAccessLogKinesisDataFirehoseDestinationOptions(BaseModel):
    Enabled: StrictBool
    DeliveryStream: StrictStr | None = None
