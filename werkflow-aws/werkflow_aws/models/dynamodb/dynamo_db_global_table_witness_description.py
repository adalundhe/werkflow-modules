from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_witness_status import DynamoDBWitnessStatus


class DynamoDBGlobalTableWitnessDescription(BaseModel):
    RegionName: StrictStr | None = None
    WitnessStatus: DynamoDBWitnessStatus | None = None
