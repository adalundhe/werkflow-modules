from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferLoggingConfiguration(BaseModel):
    LoggingRole: StrictStr | None = None
    LogGroupName: StrictStr | None = None
