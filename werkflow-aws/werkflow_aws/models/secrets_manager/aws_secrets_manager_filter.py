from __future__ import annotations
from pydantic import BaseModel, StrictStr
from typing import Literal


class AWSSecretsManagerFilter(BaseModel):
    Key: Literal[
        'description',
        'name',
        'tag-key',
        'tag-value',
        'primary-region',
        'owning-service',
        'all',
    ] | None = None
    Values: list[StrictStr] | None = None
