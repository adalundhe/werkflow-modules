from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .awss3_owner_model import AWSS3OwnerModel
from .awss3_restore_status import AWSS3RestoreStatus


class AWSS3Object(BaseModel):
    Key: StrictStr | None = None
    LastModified: datetime.datetime | StrictStr | None = None
    ETag: StrictStr | None = None
    ChecksumAlgorithm: list[StrictStr] | None = None
    ChecksumType: StrictStr | None = None
    Size: StrictInt | None = None
    StorageClass: StrictStr | None = None
    Owner: AWSS3OwnerModel | None = None
    RestoreStatus: AWSS3RestoreStatus | None = None
