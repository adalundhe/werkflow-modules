from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_request_payment_configuration import AWSS3RequestPaymentConfiguration


class AWSS3PutBucketRequestPaymentRequest(BaseModel):
    Bucket: StrictStr
    RequestPaymentConfiguration: AWSS3RequestPaymentConfiguration
    ContentMD5: StrictStr | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256', 'CRC64NVME', 'SHA512', 'MD5', 'XXHASH64', 'XXHASH3', 'XXHASH128'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
