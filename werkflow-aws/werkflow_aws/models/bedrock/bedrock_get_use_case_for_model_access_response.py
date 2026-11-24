from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes


class BedrockGetUseCaseForModelAccessResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    formData: StrictBytes | Any | None = None
    ResponseMetadata: dict[str, Any] | None = None
