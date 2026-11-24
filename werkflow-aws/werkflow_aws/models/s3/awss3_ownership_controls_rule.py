from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class AWSS3OwnershipControlsRule(BaseModel):
    ObjectOwnership: Literal['BucketOwnerPreferred', 'ObjectWriter', 'BucketOwnerEnforced'] | None = None
