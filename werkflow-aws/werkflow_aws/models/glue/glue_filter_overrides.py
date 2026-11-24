from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_between_configuration import GlueBetweenConfiguration


class GlueFilterOverrides(BaseModel):
    FieldName: StrictStr | None = None
    OperatorMappings: dict[StrictStr, StrictStr] | None = None
    BetweenConfiguration: GlueBetweenConfiguration | None = None
    DateTimeFormat: StrictStr | None = None
