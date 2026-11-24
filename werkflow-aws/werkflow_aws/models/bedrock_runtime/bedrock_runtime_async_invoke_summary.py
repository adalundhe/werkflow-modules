from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_async_invoke_output_data_config import BedrockRuntimeAsyncInvokeOutputDataConfig


class BedrockRuntimeAsyncInvokeSummary(BaseModel):
    invocationArn: StrictStr | None = None
    modelArn: StrictStr | None = None
    clientRequestToken: StrictStr | None = None
    status: StrictStr | None = None
    failureMessage: StrictStr | None = None
    submitTime: datetime.datetime | StrictStr | None = None
    lastModifiedTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    outputDataConfig: BedrockRuntimeAsyncInvokeOutputDataConfig | None = None
