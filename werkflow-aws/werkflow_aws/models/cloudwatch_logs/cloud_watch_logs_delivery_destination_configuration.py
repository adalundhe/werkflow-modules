from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeliveryDestinationConfiguration(BaseModel):
    destinationResourceArn: StrictStr | None = None
