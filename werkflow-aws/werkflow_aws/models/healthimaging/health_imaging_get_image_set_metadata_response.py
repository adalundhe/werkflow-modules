from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class HealthImagingGetImageSetMetadataResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    imageSetMetadataBlob: StrictBytes | Any | None = None
    contentType: StrictStr | None = None
    contentEncoding: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
