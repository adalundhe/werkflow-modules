import datetime
from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
)

from .aws_s3_checksum_mode import AWSS3ChecksumMode


class AWSS3GetObjectRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    IfMatch: StrictStr | None = None
    IfModifiedSince: datetime.datetime | None = None
    IfNoneMatch: StrictStr | None = None
    IfUnmodifiedSince: datetime.datetime | None = None
    Range: StrictStr | None = None
    ResponseCacheControl: StrictStr | None = None
    ResponseContentDisposition: StrictStr | None = None
    ResponseContentEncoding: StrictStr | None = None
    ResponseContentLanguage: StrictStr | None = None
    ResponseContentType: StrictStr | None = None
    ResponseExpires: datetime.datetime | None = None
    VersionId: StrictStr | None = None
    SSECustomerAlgorithm: StrictStr | None = None
    SSECustomerKey: StrictStr | None = None
    PartNumber: StrictInt | None = None
    ExpectedBucketOwner: StrictStr | None = None
    ChecksumMode: AWSS3ChecksumMode | None = None