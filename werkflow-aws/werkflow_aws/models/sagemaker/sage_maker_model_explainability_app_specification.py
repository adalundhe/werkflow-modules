from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelExplainabilityAppSpecification(BaseModel):
    ImageUri: StrictStr | None = None
    ConfigUri: StrictStr | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
