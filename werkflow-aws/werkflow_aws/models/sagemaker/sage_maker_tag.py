from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTag(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
