from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDisassociateLambdaFunctionRequest(BaseModel):
    InstanceId: StrictStr
    FunctionArn: StrictStr
    ClientToken: StrictStr | None = None
