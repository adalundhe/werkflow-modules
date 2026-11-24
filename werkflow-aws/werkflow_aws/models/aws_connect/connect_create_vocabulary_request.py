from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCreateVocabularyRequest(BaseModel):
    InstanceId: StrictStr
    VocabularyName: StrictStr
    LanguageCode: StrictStr
    Content: StrictStr
    ClientToken: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
