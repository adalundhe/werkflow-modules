from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAutoMLContainerDefinition(BaseModel):
    Image: StrictStr | None = None
    ModelDataUrl: StrictStr | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
