from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaGetProvisionedConcurrencyConfigRequest(BaseModel):
    FunctionName: StrictStr
    Qualifier: StrictStr
