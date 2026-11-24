from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictInt, StrictStr


class GlacierGetJobOutputResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    body: StrictBytes | Any | None = None
    checksum: StrictStr | None = None
    status: StrictInt | None = None
    contentRange: StrictStr | None = None
    acceptRanges: StrictStr | None = None
    contentType: StrictStr | None = None
    archiveDescription: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
