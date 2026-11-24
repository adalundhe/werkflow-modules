from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAssociateLambdaFunctionRequest(BaseModel):
    InstanceId: StrictStr
    FunctionArn: StrictStr
    ClientToken: StrictStr | None = None
