from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCfnStackDetail(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    StatusMessage: StrictStr | None = None
