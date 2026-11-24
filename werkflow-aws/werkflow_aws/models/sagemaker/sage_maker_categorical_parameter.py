from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCategoricalParameter(BaseModel):
    Name: StrictStr | None = None
    Value: list[StrictStr] | None = None
