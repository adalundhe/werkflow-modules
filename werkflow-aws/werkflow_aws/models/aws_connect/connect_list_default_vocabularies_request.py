from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListDefaultVocabulariesRequest(BaseModel):
    InstanceId: StrictStr
    LanguageCode: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
