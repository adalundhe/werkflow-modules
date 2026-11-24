from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeCustomLogSourceAttributes(BaseModel):
    crawlerArn: StrictStr | None = None
    databaseArn: StrictStr | None = None
    tableArn: StrictStr | None = None
