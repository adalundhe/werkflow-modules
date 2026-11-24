from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class LambdaInvokeWithResponseStreamRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    FunctionName: StrictStr
    LogType: Literal['None', 'Tail'] | None = None
    ClientContext: StrictStr | None = None
    Qualifier: StrictStr | None = None
    Payload: StrictBytes | BinaryIO | StrictStr | None = None
    TenantId: StrictStr | None = None
    InvocationType: Literal['RequestResponse', 'DryRun'] | None = None
