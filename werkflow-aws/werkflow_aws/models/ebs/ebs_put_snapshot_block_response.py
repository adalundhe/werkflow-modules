from pydantic import (
    BaseModel,
    StrictStr,
)
from .ebs_checksum_algorithm import EBSChecksumAlgorithm


class EBSPutSnapshotBlockResponse(BaseModel):
    Checksum: StrictStr | None = None
    ChecksumAlgorithm: EBSChecksumAlgorithm | None = None
