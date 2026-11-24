from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_between_configuration import GlueBetweenConfiguration
from .glue_filter_string_configuration import GlueFilterStringConfiguration


class GlueFilterConfiguration(BaseModel):
    FilterMode: StrictStr | None = None
    OperatorMappings: dict[StrictStr, StrictStr] | None = None
    DateTimeFormat: StrictStr | None = None
    StripQuotes: StrictBool | None = None
    BetweenConfiguration: GlueBetweenConfiguration | None = None
    FilterStringConfiguration: GlueFilterStringConfiguration | None = None
