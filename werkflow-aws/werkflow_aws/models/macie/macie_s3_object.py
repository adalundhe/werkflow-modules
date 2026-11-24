from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .macie_key_value_pair import MacieKeyValuePair
from .macie_server_side_encryption import MacieServerSideEncryption


class MacieS3Object(BaseModel):
    bucketArn: StrictStr | None = None
    eTag: StrictStr | None = None
    extension: StrictStr | None = None
    key: StrictStr | None = None
    lastModified: datetime.datetime | StrictStr | None = None
    path: StrictStr | None = None
    publicAccess: StrictBool | None = None
    serverSideEncryption: MacieServerSideEncryption | None = None
    size: StrictInt | None = None
    storageClass: StrictStr | None = None
    tags: list[MacieKeyValuePair] | None = None
    versionId: StrictStr | None = None
