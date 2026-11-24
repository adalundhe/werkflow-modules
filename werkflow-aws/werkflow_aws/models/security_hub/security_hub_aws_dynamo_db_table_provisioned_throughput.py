from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsDynamoDbTableProvisionedThroughput(BaseModel):
    LastDecreaseDateTime: StrictStr | None = None
    LastIncreaseDateTime: StrictStr | None = None
    NumberOfDecreasesToday: StrictInt | None = None
    ReadCapacityUnits: StrictInt | None = None
    WriteCapacityUnits: StrictInt | None = None
