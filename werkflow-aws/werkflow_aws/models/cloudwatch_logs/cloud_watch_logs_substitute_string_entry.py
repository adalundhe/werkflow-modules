from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field, StrictStr


class CloudWatchLogsSubstituteStringEntry(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    source: StrictStr | None = None
    from_: StrictStr | None = Field(default=None, alias='from')
    to: StrictStr | None = None
