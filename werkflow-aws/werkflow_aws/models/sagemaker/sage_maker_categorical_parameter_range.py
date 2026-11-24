from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCategoricalParameterRange(BaseModel):
    Name: StrictStr | None = None
    Values: list[StrictStr] | None = None
