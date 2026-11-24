from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class BedrockRuntimeInvokeModelRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    modelId: StrictStr
    body: StrictBytes | BinaryIO | StrictStr | None = None
    contentType: StrictStr | None = None
    accept: StrictStr | None = None
    trace: Literal['ENABLED', 'DISABLED', 'ENABLED_FULL'] | None = None
    guardrailIdentifier: StrictStr | None = None
    guardrailVersion: StrictStr | None = None
    performanceConfigLatency: Literal['standard', 'optimized'] | None = None
    serviceTier: Literal['priority', 'default', 'flex', 'reserved'] | None = None
    requestMetadata: StrictStr | None = None
    projectIdentifier: StrictStr | None = None
