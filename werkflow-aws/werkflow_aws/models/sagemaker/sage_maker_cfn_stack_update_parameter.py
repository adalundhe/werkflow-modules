from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCfnStackUpdateParameter(BaseModel):
    Key: StrictStr
    Value: StrictStr | None = None
