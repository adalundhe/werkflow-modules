from __future__ import annotations
from pydantic import BaseModel, StrictInt


class KinesisS3TablesDestinationUpdateInput(BaseModel):
    DataFreshnessInSeconds: StrictInt
