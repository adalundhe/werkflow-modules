from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferStartRemoteMoveRequest(BaseModel):
    ConnectorId: StrictStr
    SourcePath: StrictStr
    TargetPath: StrictStr
