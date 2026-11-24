from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAssociateDefaultVocabularyRequest(BaseModel):
    InstanceId: StrictStr
    LanguageCode: StrictStr
    VocabularyId: StrictStr | None = None
