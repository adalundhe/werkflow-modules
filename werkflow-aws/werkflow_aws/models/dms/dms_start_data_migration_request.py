from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DMSStartDataMigrationRequest(BaseModel):
    DataMigrationIdentifier: StrictStr
    StartType: Literal['reload-target', 'resume-processing', 'start-replication']
