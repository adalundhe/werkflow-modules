from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncAzureBlobSasConfiguration(BaseModel):
    Token: StrictStr
