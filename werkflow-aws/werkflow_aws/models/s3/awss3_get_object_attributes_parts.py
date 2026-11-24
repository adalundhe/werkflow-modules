from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .awss3_object_part import AWSS3ObjectPart


class AWSS3GetObjectAttributesParts(BaseModel):
    TotalPartsCount: StrictInt | None = None
    PartNumberMarker: StrictInt | None = None
    NextPartNumberMarker: StrictInt | None = None
    MaxParts: StrictInt | None = None
    IsTruncated: StrictBool | None = None
    Parts: list[AWSS3ObjectPart] | None = None
