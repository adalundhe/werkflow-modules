from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TransferSftpConnectorConfig(BaseModel):
    UserSecretId: StrictStr | None = None
    TrustedHostKeys: list[StrictStr] | None = None
    MaxConcurrentConnections: StrictInt | None = None
    OrderedUserSecretVersionStages: list[StrictStr] | None = None
