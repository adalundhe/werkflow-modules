from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class SSMDeleteInventoryRequest(BaseModel):
    TypeName: StrictStr
    SchemaDeleteOption: Literal['DisableSchema', 'DeleteSchema'] | None = None
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
