from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .personalize_tag import PersonalizeTag


class PersonalizeCreateSolutionVersionRequest(BaseModel):
    solutionArn: StrictStr
    name: StrictStr | None = None
    trainingMode: Literal['FULL', 'UPDATE', 'AUTOTRAIN'] | None = None
    tags: list[PersonalizeTag] | None = None
