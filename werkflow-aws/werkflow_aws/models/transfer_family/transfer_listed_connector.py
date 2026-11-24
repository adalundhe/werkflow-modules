from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferListedConnector(BaseModel):
    Arn: StrictStr | None = None
    ConnectorId: StrictStr | None = None
    Url: StrictStr | None = None
