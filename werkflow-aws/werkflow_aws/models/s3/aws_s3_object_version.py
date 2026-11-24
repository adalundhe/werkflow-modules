import datetime
from typing import Dict, List, Literal
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr


class AWSs3ObjectVersion(BaseModel):
    ETag: StrictStr | None = None
    ChecksumAlgorithm: List[Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256']] = Field(
        default_factory=list
    )
    Size: StrictInt | None = None
    StorageClass: StrictStr | None = None
    Key: StrictStr | None = None
    VersionId: StrictStr | None = None
    IsLatest: StrictBool | None = None
    LastModified: datetime.datetime | None = None
    Owner: Dict[Literal['DisplayName', 'ID'], StrictStr] | None = None
    RestoreStatus: Dict[
        Literal['IsRestoreInProgress', 'RestoreExpiryDate'],
        StrictBool | datetime.datetime,
    ] | None = None
