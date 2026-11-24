from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class BedrockRuntimeInvokeModelResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    body: StrictBytes | Any | None = None
    contentType: StrictStr | None = None
    performanceConfigLatency: StrictStr | None = None
    serviceTier: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
