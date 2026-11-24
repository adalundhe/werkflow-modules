from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class KinesisVideoGetDataEndpointRequest(BaseModel):
    APIName: Literal['PUT_MEDIA', 'GET_MEDIA', 'LIST_FRAGMENTS', 'GET_MEDIA_FOR_FRAGMENT_LIST', 'GET_HLS_STREAMING_SESSION_URL', 'GET_DASH_STREAMING_SESSION_URL', 'GET_CLIP', 'GET_IMAGES']
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
