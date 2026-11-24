from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictInt
from .filter_subscription import FilterSubscription


class FilterSubscriptionsList(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    end_index: StrictInt | None = PydanticField(default=None, alias='end-index')
    items: list[FilterSubscription] | None = None
    max_results: StrictInt | None = PydanticField(default=None, alias='max-results')
    size: StrictInt | None = None
    start_index: StrictInt | None = PydanticField(default=None, alias='start-index')
