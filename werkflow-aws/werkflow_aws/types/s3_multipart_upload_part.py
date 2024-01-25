from typing import TypedDict, Optional


class s3MultipartUploadPart(TypedDict):
    ETag: str
    ChecksumCRC32: Optional[str]
    ChecksumCRC32C: Optional[str]
    ChecksumSHA1: Optional[str]
    ChecksumSHA256: Optional[str]
    PartNumber: int