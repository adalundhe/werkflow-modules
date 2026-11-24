from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBEnableKinesisStreamingConfiguration(BaseModel):
    ApproximateCreationDateTimePrecision: StrictStr | None = None
