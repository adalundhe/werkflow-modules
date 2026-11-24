from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, StrictStr


class APIGatewayPatchOperation(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    op: Literal['add', 'remove', 'replace', 'move', 'copy', 'test'] | None = None
    path: StrictStr | None = None
    value: StrictStr | None = None
    from_: StrictStr | None = Field(default=None, alias='from')
