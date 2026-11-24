from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueDataLakeAccessProperties(BaseModel):
    DataLakeAccess: StrictBool | None = None
    DataTransferRole: StrictStr | None = None
    KmsKey: StrictStr | None = None
    CatalogType: StrictStr | None = None
