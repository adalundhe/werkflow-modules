from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectVocabularySummary(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    State: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
