from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class HealthImagingGetImageFrameResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    imageFrameBlob: StrictBytes | Any | None = None
    contentType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
