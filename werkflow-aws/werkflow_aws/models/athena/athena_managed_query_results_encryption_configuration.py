from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaManagedQueryResultsEncryptionConfiguration(BaseModel):
    KmsKey: StrictStr | None = None
