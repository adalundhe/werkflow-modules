from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockListInferenceProfilesRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    typeEquals: Literal['SYSTEM_DEFINED', 'APPLICATION'] | None = None
    projectIdentifier: StrictStr | None = None
