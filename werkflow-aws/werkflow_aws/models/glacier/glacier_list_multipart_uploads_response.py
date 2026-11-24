from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glacier_upload_list_element import GlacierUploadListElement


class GlacierListMultipartUploadsResponse(BaseModel):
    UploadsList: list[GlacierUploadListElement] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
