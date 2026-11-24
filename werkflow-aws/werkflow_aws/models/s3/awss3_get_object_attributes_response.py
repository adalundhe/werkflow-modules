from __future__ import annotations
import datetime
from typing import Any, Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .awss3_checksum import AWSS3Checksum
from .awss3_get_object_attributes_parts import AWSS3GetObjectAttributesParts


class AWSS3GetObjectAttributesResponse(BaseModel):
    DeleteMarker: StrictBool | None = None
    LastModified: datetime.datetime | None = None
    VersionId: StrictStr | None = None
    RequestCharged: Literal['requester'] | None = None
    ETag: StrictStr | None = None
    Checksum: AWSS3Checksum | None = None
    ObjectParts: AWSS3GetObjectAttributesParts | None = None
    StorageClass: Literal['STANDARD', 'REDUCED_REDUNDANCY', 'STANDARD_IA', 'ONEZONE_IA', 'INTELLIGENT_TIERING', 'GLACIER', 'DEEP_ARCHIVE', 'OUTPOSTS', 'GLACIER_IR', 'SNOW', 'EXPRESS_ONEZONE', 'FSX_OPENZFS', 'FSX_ONTAP', 'AWS_BACKUP_WARM', 'AWS_BACKUP_LOW_COST_WARM'] | None = None
    ObjectSize: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
