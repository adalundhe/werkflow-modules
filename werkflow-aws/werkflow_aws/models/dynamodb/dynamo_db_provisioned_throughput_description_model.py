from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class DynamoDBProvisionedThroughputDescriptionModel(BaseModel):
    LastIncreaseDateTime: datetime.datetime | StrictStr | None = None
    LastDecreaseDateTime: datetime.datetime | StrictStr | None = None
    NumberOfDecreasesToday: StrictInt | None = None
    ReadCapacityUnits: StrictInt | None = None
    WriteCapacityUnits: StrictInt | None = None
