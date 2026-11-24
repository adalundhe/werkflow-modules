from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class AWSS3OwnershipControlsRuleInput(BaseModel):
    ObjectOwnership: Literal['BucketOwnerPreferred', 'ObjectWriter', 'BucketOwnerEnforced']
