from pydantic import BaseModel
from .ebs_status import EBSStatus


class EBSCompleteSnapshotResponse(BaseModel):
    Status: EBSStatus | None = None
