from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerQueryFilters(BaseModel):
    Types: list[StrictStr] | None = None
    LineageTypes: list[Literal['TrialComponent', 'Artifact', 'Context', 'Action']] | None = None
    CreatedBefore: datetime.datetime | StrictStr | None = None
    CreatedAfter: datetime.datetime | StrictStr | None = None
    ModifiedBefore: datetime.datetime | StrictStr | None = None
    ModifiedAfter: datetime.datetime | StrictStr | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
