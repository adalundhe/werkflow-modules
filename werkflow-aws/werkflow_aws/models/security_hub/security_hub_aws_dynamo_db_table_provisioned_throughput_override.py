from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubAwsDynamoDbTableProvisionedThroughputOverride(BaseModel):
    ReadCapacityUnits: StrictInt | None = None
