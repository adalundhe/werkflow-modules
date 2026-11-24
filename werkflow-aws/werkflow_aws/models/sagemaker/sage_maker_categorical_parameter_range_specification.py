from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCategoricalParameterRangeSpecification(BaseModel):
    Values: list[StrictStr] | None = None
