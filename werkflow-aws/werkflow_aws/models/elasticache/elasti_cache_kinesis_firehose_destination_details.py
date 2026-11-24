from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheKinesisFirehoseDestinationDetails(BaseModel):
    DeliveryStream: StrictStr | None = None
