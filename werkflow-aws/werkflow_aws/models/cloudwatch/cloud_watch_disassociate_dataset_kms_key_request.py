from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchDisassociateDatasetKmsKeyRequest(BaseModel):
    DatasetIdentifier: StrictStr
