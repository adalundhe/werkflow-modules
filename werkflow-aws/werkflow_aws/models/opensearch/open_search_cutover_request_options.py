from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class OpenSearchCutoverRequestOptions(BaseModel):
    Target: Literal['ClonedCluster', 'PrimaryCluster']
