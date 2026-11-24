from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRRepositoryScanningConfigurationFailure(BaseModel):
    repositoryName: StrictStr | None = None
    failureCode: StrictStr | None = None
    failureReason: StrictStr | None = None
