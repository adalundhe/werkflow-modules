from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCfnStackCreateParameter(BaseModel):
    Key: StrictStr
    Value: StrictStr | None = None
