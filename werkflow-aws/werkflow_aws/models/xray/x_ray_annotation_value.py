from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class XRayAnnotationValue(BaseModel):
    NumberValue: StrictFloat | StrictInt | None = None
    BooleanValue: StrictBool | None = None
    StringValue: StrictStr | None = None
