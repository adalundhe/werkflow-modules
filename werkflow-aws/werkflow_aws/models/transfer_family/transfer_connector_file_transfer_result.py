from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferConnectorFileTransferResult(BaseModel):
    FilePath: StrictStr | None = None
    StatusCode: StrictStr | None = None
    FailureCode: StrictStr | None = None
    FailureMessage: StrictStr | None = None
