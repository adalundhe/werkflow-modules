from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBTimeToLiveDescriptionModel(BaseModel):
    TimeToLiveStatus: StrictStr | None = None
    AttributeName: StrictStr | None = None
