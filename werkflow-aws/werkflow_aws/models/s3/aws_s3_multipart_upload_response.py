import datetime
from pydantic import (
    BaseModel,
    StrictStr
)
from typing import Dict, Literal


class AWSs3MultipartUploadResponse(BaseModel):
    UploadId: StrictStr | None = None
    Key: StrictStr | None = None
    Initiated: datetime.datetime | None = None
    StorageClass: Literal['STANDARD', 'REDUCED_REDUNDANCY', 'STANDARD_IA', 'ONEZONE_IA', 'INTELLIGENT_TIERING', 'GLACIER', 'DEEP_ARCHIVE', 'OUTPOSTS', 'GLACIER_IR', 'SNOW', 'EXPRESS_ONEZONE'] | None = None
    Owner: Dict[Literal['DisplayName', 'ID'], StrictStr] | None = None
    Initiator: Dict[Literal['ID', 'DisplayName'], StrictStr] | None = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256'] | None = None
