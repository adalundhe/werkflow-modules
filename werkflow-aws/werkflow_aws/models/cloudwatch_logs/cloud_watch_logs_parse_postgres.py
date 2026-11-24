from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsParsePostgres(BaseModel):
    source: StrictStr | None = None
