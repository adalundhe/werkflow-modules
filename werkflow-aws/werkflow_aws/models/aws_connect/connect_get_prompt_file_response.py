from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectGetPromptFileResponse(BaseModel):
    PromptPresignedUrl: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
