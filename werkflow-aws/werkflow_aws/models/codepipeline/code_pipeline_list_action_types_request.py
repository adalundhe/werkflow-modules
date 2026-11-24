from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodePipelineListActionTypesRequest(BaseModel):
    actionOwnerFilter: Literal['AWS', 'ThirdParty', 'Custom'] | None = None
    nextToken: StrictStr | None = None
    regionFilter: StrictStr | None = None
