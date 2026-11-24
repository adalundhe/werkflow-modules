from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .awss3_common_prefix import AWSS3CommonPrefix
from .awss3_object import AWSS3Object


class AWSS3ListObjectsResponseModel(BaseModel):
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    NextMarker: StrictStr | None = None
    Contents: list[AWSS3Object] | None = None
    Name: StrictStr | None = None
    Prefix: StrictStr | None = None
    Delimiter: StrictStr | None = None
    MaxKeys: StrictInt | None = None
    CommonPrefixes: list[AWSS3CommonPrefix] | None = None
    EncodingType: StrictStr | None = None
    RequestCharged: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
