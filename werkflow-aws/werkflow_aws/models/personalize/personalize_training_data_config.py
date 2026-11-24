from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeTrainingDataConfig(BaseModel):
    excludedDatasetColumns: dict[StrictStr, list[StrictStr]] | None = None
    includedDatasetColumns: dict[StrictStr, list[StrictStr]] | None = None
