from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueCascadingOption(BaseModel):
    cascadingOptionId: StrictStr | None = None
    contextId: StrictStr | None = None
    optionId: StrictStr | None = None
    type: StrictStr | None = None
