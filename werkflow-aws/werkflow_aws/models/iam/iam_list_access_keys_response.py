from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_access_key_metadata import IAMAccessKeyMetadata


class IAMListAccessKeysResponse(BaseModel):
    AccessKeyMetadata: list[IAMAccessKeyMetadata] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
