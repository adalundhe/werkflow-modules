from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchS3GlueDataCatalog(BaseModel):
    RoleArn: StrictStr | None = None
