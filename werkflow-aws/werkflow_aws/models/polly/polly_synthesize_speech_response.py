from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictInt, StrictStr


class PollySynthesizeSpeechResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    AudioStream: StrictBytes | Any | None = None
    ContentType: StrictStr | None = None
    RequestCharacters: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
