from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBKinesisDataStreamDestination(BaseModel):
    StreamArn: StrictStr | None = None
    DestinationStatus: StrictStr | None = None
    DestinationStatusDescription: StrictStr | None = None
    ApproximateCreationDateTimePrecision: StrictStr | None = None
