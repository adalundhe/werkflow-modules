from __future__ import annotations
from pydantic import BaseModel
from .awss3_ownership_controls_rule import AWSS3OwnershipControlsRule


class AWSS3OwnershipControls(BaseModel):
    Rules: list[AWSS3OwnershipControlsRule] | None = None
