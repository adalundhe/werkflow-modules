from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeVocabularyRequest(BaseModel):
    InstanceId: StrictStr
    VocabularyId: StrictStr
