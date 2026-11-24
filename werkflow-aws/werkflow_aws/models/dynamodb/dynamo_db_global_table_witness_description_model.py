from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBGlobalTableWitnessDescriptionModel(BaseModel):
    RegionName: StrictStr | None = None
    WitnessStatus: StrictStr | None = None
