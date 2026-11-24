from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodeCatalystListSourceRepositoriesItem(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    lastUpdatedTime: datetime.datetime | StrictStr | None = None
    createdTime: datetime.datetime | StrictStr | None = None
