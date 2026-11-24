from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerFilterModel(BaseModel):
    Key: Literal['description', 'name', 'tag-key', 'tag-value', 'primary-region', 'owning-service', 'all'] | None = None
    Values: list[StrictStr] | None = None
