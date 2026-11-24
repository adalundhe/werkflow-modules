from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_unprocessed_scram_secret import MSKUnprocessedScramSecret


class MSKBatchDisassociateScramSecretResponse(BaseModel):
    ClusterArn: StrictStr | None = None
    UnprocessedScramSecrets: list[MSKUnprocessedScramSecret] | None = None
    ResponseMetadata: dict[str, Any] | None = None
