from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .lambda_invoke_with_response_stream_response_event import LambdaInvokeWithResponseStreamResponseEvent


class LambdaInvokeWithResponseStreamResponse(BaseModel):
    StatusCode: StrictInt | None = None
    ExecutedVersion: StrictStr | None = None
    EventStream: LambdaInvokeWithResponseStreamResponseEvent | None = None
    ResponseStreamContentType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
