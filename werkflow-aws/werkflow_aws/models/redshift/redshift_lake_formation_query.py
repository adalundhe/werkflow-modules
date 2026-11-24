from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftLakeFormationQuery(BaseModel):
    Authorization: StrictStr | None = None
