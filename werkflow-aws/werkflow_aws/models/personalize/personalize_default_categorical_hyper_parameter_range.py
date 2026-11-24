from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class PersonalizeDefaultCategoricalHyperParameterRange(BaseModel):
    name: StrictStr | None = None
    values: list[StrictStr] | None = None
    isTunable: StrictBool | None = None
