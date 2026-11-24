from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AthenaUpdateSystemTableConfigurationRequest(BaseModel):
    TableName: Literal['ALL']
    KmsKeyArn: StrictStr | None = None
