from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3Checksum(BaseModel):
    ChecksumCRC32: StrictStr | None = None
    ChecksumCRC32C: StrictStr | None = None
    ChecksumCRC64NVME: StrictStr | None = None
    ChecksumSHA1: StrictStr | None = None
    ChecksumSHA256: StrictStr | None = None
    ChecksumSHA512: StrictStr | None = None
    ChecksumMD5: StrictStr | None = None
    ChecksumXXHASH64: StrictStr | None = None
    ChecksumXXHASH3: StrictStr | None = None
    ChecksumXXHASH128: StrictStr | None = None
    ChecksumType: Literal['COMPOSITE', 'FULL_OBJECT'] | None = None
