from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class QBusinessGetMediaResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    mediaBytes: StrictBytes | Any | None = None
    mediaMimeType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
