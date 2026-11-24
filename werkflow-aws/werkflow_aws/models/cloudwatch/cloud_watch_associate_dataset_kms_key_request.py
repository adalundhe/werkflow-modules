from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchAssociateDatasetKmsKeyRequest(BaseModel):
    DatasetIdentifier: StrictStr
    KmsKeyArn: StrictStr
