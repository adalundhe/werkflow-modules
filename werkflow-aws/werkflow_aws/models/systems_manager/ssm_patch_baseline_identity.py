from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SSMPatchBaselineIdentity(BaseModel):
    BaselineId: StrictStr | None = None
    BaselineName: StrictStr | None = None
    OperatingSystem: StrictStr | None = None
    BaselineDescription: StrictStr | None = None
    DefaultBaseline: StrictBool | None = None
