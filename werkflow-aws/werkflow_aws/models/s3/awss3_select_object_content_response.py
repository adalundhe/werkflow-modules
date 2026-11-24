from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_select_object_content_event_stream import AWSS3SelectObjectContentEventStream


class AWSS3SelectObjectContentResponse(BaseModel):
    Payload: AWSS3SelectObjectContentEventStream | None = None
    ResponseMetadata: dict[str, Any] | None = None
