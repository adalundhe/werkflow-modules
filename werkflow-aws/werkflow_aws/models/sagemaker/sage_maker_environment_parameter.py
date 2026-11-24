from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEnvironmentParameter(BaseModel):
    Key: StrictStr | None = None
    ValueType: StrictStr | None = None
    Value: StrictStr | None = None
