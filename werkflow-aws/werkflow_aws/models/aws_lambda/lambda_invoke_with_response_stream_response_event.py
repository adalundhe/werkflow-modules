from __future__ import annotations
from pydantic import BaseModel
from .lambda_invoke_response_stream_update import LambdaInvokeResponseStreamUpdate
from .lambda_invoke_with_response_stream_complete_event import LambdaInvokeWithResponseStreamCompleteEvent


class LambdaInvokeWithResponseStreamResponseEvent(BaseModel):
    PayloadChunk: LambdaInvokeResponseStreamUpdate | None = None
    InvokeComplete: LambdaInvokeWithResponseStreamCompleteEvent | None = None
