from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TransferListFileTransferResultsRequest(BaseModel):
    ConnectorId: StrictStr
    TransferId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
