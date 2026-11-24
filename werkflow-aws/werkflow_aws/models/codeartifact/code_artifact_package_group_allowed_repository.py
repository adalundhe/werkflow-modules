from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeArtifactPackageGroupAllowedRepository(BaseModel):
    repositoryName: StrictStr | None = None
    originRestrictionType: Literal['EXTERNAL_UPSTREAM', 'INTERNAL_UPSTREAM', 'PUBLISH'] | None = None
