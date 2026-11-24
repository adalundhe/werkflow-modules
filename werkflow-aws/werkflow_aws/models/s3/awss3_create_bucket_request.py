from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from typing import Literal
from .awss3_create_bucket_configuration import AWSS3CreateBucketConfiguration


class AWSS3CreateBucketRequest(BaseModel):
    Bucket: StrictStr | None = None
    ACL: Literal['private', 'public-read', 'public-read-write', 'authenticated-read'] | None = None
    CreateBucketConfiguration: AWSS3CreateBucketConfiguration | None = None
    GrantFullControl: StrictStr | None = None
    GrantRead: StrictStr | None = None
    GrantReadACP: StrictStr | None = None
    GrantWrite: StrictStr | None = None
    GrantWriteACP: StrictStr | None = None
    ObjectLockEnabledForBucket: StrictBool | None = None
    ObjectOwnership: Literal['BucketOwnerPreferred', 'ObjectWriter', 'BucketOwnerEnforced'] | None = None
