from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferAs2AsyncMdnConnectorConfig(BaseModel):
    Url: StrictStr | None = None
    ServerIds: list[StrictStr] | None = None
