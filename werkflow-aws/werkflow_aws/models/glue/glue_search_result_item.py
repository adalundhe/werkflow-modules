from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GlueSearchResultItem(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    AssetTypeId: StrictStr | None = None
