from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class PollyLexiconAttributes(BaseModel):
    Alphabet: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    LastModified: datetime.datetime | StrictStr | None = None
    LexiconArn: StrictStr | None = None
    LexemesCount: StrictInt | None = None
    Size: StrictInt | None = None
