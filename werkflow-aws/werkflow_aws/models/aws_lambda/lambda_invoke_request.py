from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from typing import BinaryIO
from .lambda_invocation_type import LambdaInvocationType
from .lambda_log_type import LambdaLogType


class LambdaInvokeRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    FunctionName: StrictStr
    InvocationType: LambdaInvocationType | None = None
    LogType: LambdaLogType | None = None
    ClientContext: StrictStr | None = None
    DurableExecutionName: StrictStr | None = None
    Payload: StrictBytes | StrictStr | BinaryIO | None = None
    Qualifier: StrictStr | None = None
    TenantId: StrictStr | None = None
