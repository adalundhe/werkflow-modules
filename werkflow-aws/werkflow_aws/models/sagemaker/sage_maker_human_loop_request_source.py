from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerHumanLoopRequestSource(BaseModel):
    AwsManagedHumanLoopRequestSource: StrictStr | None = None
