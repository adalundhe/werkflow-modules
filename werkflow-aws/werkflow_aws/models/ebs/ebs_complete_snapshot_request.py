from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
)
from .ebs_checksum_aggregation_method import EBSChecksumAggregationMethod
from .ebs_checksum_algorithm import EBSChecksumAlgorithm


class EBSCompleteSnapshotRequest(BaseModel):
    SnapshotId: StrictStr
    ChangedBlocksCount: StrictInt
    Checksum: StrictStr | None = None
    ChecksumAlgorithm: EBSChecksumAlgorithm | None = None
    ChecksumAggregationMethod: EBSChecksumAggregationMethod | None = None
