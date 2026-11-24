from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerClusterMetadata(BaseModel):
    FailureMessage: StrictStr | None = None
    EksRoleAccessEntries: list[StrictStr] | None = None
    SlrAccessEntry: StrictStr | None = None
