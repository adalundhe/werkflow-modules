from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRBatchGetRepositoryScanningConfigurationRequest(BaseModel):
    repositoryNames: list[StrictStr]
