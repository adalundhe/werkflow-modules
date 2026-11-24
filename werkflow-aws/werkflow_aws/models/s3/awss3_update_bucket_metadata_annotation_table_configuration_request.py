from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_annotation_table_configuration_updates import AWSS3AnnotationTableConfigurationUpdates


class AWSS3UpdateBucketMetadataAnnotationTableConfigurationRequest(BaseModel):
    Bucket: StrictStr
    AnnotationTableConfiguration: AWSS3AnnotationTableConfigurationUpdates
    ContentMD5: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
