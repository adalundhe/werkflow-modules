from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESKinesisFirehoseDestination(BaseModel):
    IamRoleArn: StrictStr | None = None
    DeliveryStreamArn: StrictStr | None = None
