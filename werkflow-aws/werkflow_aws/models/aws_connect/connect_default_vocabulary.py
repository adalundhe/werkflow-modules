from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDefaultVocabulary(BaseModel):
    InstanceId: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    VocabularyId: StrictStr | None = None
    VocabularyName: StrictStr | None = None
