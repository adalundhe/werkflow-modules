from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDeleteTieringConfigurationRequest(BaseModel):
    TieringConfigurationName: StrictStr
