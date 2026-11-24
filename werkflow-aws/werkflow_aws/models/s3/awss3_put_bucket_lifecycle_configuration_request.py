from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_bucket_lifecycle_configuration import AWSS3BucketLifecycleConfiguration


class AWSS3PutBucketLifecycleConfigurationRequest(BaseModel):
    Bucket: StrictStr
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
    LifecycleConfiguration: AWSS3BucketLifecycleConfiguration | None = None
    ExpectedBucketOwner: StrictStr | None = None
    TransitionDefaultMinimumObjectSize: Literal['varies_by_storage_class', 'all_storage_classes_128K'] | None = None
