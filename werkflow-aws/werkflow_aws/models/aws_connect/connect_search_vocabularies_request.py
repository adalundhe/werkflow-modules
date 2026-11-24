from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectSearchVocabulariesRequest(BaseModel):
    InstanceId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    State: Literal['CREATION_IN_PROGRESS', 'ACTIVE', 'CREATION_FAILED', 'DELETE_IN_PROGRESS'] | None = None
    NameStartsWith: StrictStr | None = None
    LanguageCode: StrictStr | None = None
