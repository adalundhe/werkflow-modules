from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDatabaseConfigurationMetadata(BaseModel):
    RollbackStatus: StrictStr | None = None
    Advisory: StrictStr | None = None
    FailureMessage: StrictStr | None = None
