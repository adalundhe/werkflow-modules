from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaPutProvisionedConcurrencyConfigRequest(BaseModel):
    FunctionName: StrictStr
    Qualifier: StrictStr
    ProvisionedConcurrentExecutions: StrictInt
