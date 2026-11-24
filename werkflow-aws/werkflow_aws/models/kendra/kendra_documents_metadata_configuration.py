from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDocumentsMetadataConfiguration(BaseModel):
    S3Prefix: StrictStr | None = None
