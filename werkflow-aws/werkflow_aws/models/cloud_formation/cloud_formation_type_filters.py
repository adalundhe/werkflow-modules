from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationTypeFilters(BaseModel):
    Category: Literal['REGISTERED', 'ACTIVATED', 'THIRD_PARTY', 'AWS_TYPES'] | None = None
    PublisherId: StrictStr | None = None
    TypeNamePrefix: StrictStr | None = None
