from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueCodeGenNodeArg(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
    Param: StrictBool | None = None
