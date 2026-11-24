from __future__ import annotations
from pydantic import BaseModel
from .macie_s3_destination import MacieS3Destination


class MacieClassificationExportConfiguration(BaseModel):
    s3Destination: MacieS3Destination | None = None
