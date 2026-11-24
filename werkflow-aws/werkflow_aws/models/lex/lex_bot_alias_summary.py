from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexBotAliasSummary(BaseModel):
    botAliasId: StrictStr | None = None
    botAliasName: StrictStr | None = None
    description: StrictStr | None = None
    botVersion: StrictStr | None = None
    botAliasStatus: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
