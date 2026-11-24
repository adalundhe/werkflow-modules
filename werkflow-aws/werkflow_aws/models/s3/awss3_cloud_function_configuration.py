from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3CloudFunctionConfiguration(BaseModel):
    Id: StrictStr | None = None
    Event: StrictStr | None = None
    Events: list[StrictStr] | None = None
    CloudFunction: StrictStr | None = None
    InvocationRole: StrictStr | None = None
