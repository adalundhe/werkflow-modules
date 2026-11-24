from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .glacier_part_list_element import GlacierPartListElement


class GlacierListPartsResponse(BaseModel):
    MultipartUploadId: StrictStr | None = None
    VaultARN: StrictStr | None = None
    ArchiveDescription: StrictStr | None = None
    PartSizeInBytes: StrictInt | None = None
    CreationDate: StrictStr | None = None
    Parts: list[GlacierPartListElement] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
