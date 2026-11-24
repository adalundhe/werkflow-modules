from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class GlueCatalogImportStatus(BaseModel):
    ImportCompleted: StrictBool | None = None
    ImportTime: datetime.datetime | StrictStr | None = None
    ImportedBy: StrictStr | None = None
