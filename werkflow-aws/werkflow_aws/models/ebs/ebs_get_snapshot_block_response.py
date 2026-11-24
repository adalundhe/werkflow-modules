from botocore.response import StreamingBody
from pydantic import (
    BaseModel,
    ConfigDict,
    StrictBytes,
    StrictInt,
    StrictStr,
)
from .ebs_checksum_algorithm import EBSChecksumAlgorithm


class EBSGetSnapshotBlockResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    DataLength: StrictInt | None = None
    BlockData: StreamingBody | StrictBytes | None = None
    Checksum: StrictStr | None = None
    ChecksumAlgorithm: EBSChecksumAlgorithm | None = None
