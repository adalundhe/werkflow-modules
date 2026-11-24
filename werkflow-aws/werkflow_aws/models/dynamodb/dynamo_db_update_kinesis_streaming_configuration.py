from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBUpdateKinesisStreamingConfiguration(BaseModel):
    ApproximateCreationDateTimePrecision: StrictStr | None = None
