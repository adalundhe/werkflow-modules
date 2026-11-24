from __future__ import annotations
from botocore.response import StreamingBody
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictInt, StrictStr


class LambdaInvokeResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    StatusCode: StrictInt | None = None
    FunctionError: StrictStr | None = None
    LogResult: StrictStr | None = None
    Payload: StreamingBody | StrictBytes | None = None
    ExecutedVersion: StrictStr | None = None
    DurableExecutionArn: StrictStr | None = None
