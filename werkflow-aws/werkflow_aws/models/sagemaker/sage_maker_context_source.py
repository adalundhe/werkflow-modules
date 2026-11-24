from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerContextSource(BaseModel):
    SourceUri: StrictStr | None = None
    SourceType: StrictStr | None = None
    SourceId: StrictStr | None = None
