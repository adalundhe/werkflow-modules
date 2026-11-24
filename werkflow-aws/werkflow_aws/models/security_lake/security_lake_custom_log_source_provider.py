from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeCustomLogSourceProvider(BaseModel):
    location: StrictStr | None = None
    roleArn: StrictStr | None = None
