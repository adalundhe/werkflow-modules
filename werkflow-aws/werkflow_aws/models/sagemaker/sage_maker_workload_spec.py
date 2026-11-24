from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerWorkloadSpec(BaseModel):
    Inline: StrictStr | None = None
