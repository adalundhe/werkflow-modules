from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteVocabularyRequest(BaseModel):
    InstanceId: StrictStr
    VocabularyId: StrictStr
