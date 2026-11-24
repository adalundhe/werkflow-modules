from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationExternalFilteringConfiguration(BaseModel):
    Status: StrictStr | None = None
    AuthorizedTargets: list[StrictStr] | None = None
