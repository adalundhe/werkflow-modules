from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class TranscribeUpdateLanguageModelResponse(BaseModel):
    ModelName: StrictStr | None = None
    ModelStatus: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
