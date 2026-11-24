from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .kendra_expand_configuration import KendraExpandConfiguration
from .kendra_sorting_configuration import KendraSortingConfiguration


class KendraCollapseConfiguration(BaseModel):
    DocumentAttributeKey: StrictStr
    SortingConfigurations: list[KendraSortingConfiguration] | None = None
    MissingAttributeKeyStrategy: Literal['IGNORE', 'COLLAPSE', 'EXPAND'] | None = None
    Expand: StrictBool | None = None
    ExpandConfiguration: KendraExpandConfiguration | None = None
