from typing import BinaryIO
from pydantic import (
    BaseModel,
    ConfigDict,
    StrictBytes,
    StrictInt,
    StrictStr,
)
from .ebs_checksum_algorithm import EBSChecksumAlgorithm


class EBSPutSnapshotBlockRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    SnapshotId: StrictStr
    BlockIndex: StrictInt
    BlockData: StrictBytes | BinaryIO
    DataLength: StrictInt
    Checksum: StrictStr
    ChecksumAlgorithm: EBSChecksumAlgorithm
    Progress: StrictInt | None = None
