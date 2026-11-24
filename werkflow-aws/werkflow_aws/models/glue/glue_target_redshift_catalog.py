from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueTargetRedshiftCatalog(BaseModel):
    CatalogArn: StrictStr | None = None
