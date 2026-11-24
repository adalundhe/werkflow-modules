from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneRedshiftCredentialConfiguration(BaseModel):
    secretManagerArn: StrictStr | None = None
