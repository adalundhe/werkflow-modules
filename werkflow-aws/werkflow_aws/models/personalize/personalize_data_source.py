from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDataSource(BaseModel):
    dataLocation: StrictStr | None = None
