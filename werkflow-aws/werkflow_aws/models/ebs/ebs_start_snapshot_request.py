from pydantic import (
    BaseModel,
    StrictBool,
    StrictInt,
    StrictStr,
)
from .ebs_tag import EBSTag


class EBSStartSnapshotRequest(BaseModel):
    VolumeSize: StrictInt
    ParentSnapshotId: StrictStr | None = None
    Tags: list[EBSTag] | None = None
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
    Encrypted: StrictBool | None = None
    KmsKeyArn: StrictStr | None = None
    Timeout: StrictInt | None = None
