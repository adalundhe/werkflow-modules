from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .macie_bucket_public_access import MacieBucketPublicAccess
from .macie_key_value_pair import MacieKeyValuePair
from .macie_s3_bucket_owner import MacieS3BucketOwner
from .macie_server_side_encryption import MacieServerSideEncryption


class MacieS3Bucket(BaseModel):
    allowsUnencryptedObjectUploads: StrictStr | None = None
    arn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    defaultServerSideEncryption: MacieServerSideEncryption | None = None
    name: StrictStr | None = None
    owner: MacieS3BucketOwner | None = None
    publicAccess: MacieBucketPublicAccess | None = None
    tags: list[MacieKeyValuePair] | None = None
