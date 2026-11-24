from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .kendra_attribute_suggestions_update_config import KendraAttributeSuggestionsUpdateConfig


class KendraUpdateQuerySuggestionsConfigRequest(BaseModel):
    IndexId: StrictStr
    Mode: Literal['ENABLED', 'LEARN_ONLY'] | None = None
    QueryLogLookBackWindowInDays: StrictInt | None = None
    IncludeQueriesWithoutUserInformation: StrictBool | None = None
    MinimumNumberOfQueryingUsers: StrictInt | None = None
    MinimumQueryCount: StrictInt | None = None
    AttributeSuggestionsConfig: KendraAttributeSuggestionsUpdateConfig | None = None
