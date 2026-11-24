from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaDeleteProvisionedConcurrencyConfigRequest(BaseModel):
    FunctionName: StrictStr
    Qualifier: StrictStr
