from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTrialSource(BaseModel):
    SourceArn: StrictStr | None = None
    SourceType: StrictStr | None = None
