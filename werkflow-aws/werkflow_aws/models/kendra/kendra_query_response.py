from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .kendra_facet_result import KendraFacetResult
from .kendra_featured_results_item import KendraFeaturedResultsItem
from .kendra_query_result_item import KendraQueryResultItem
from .kendra_spell_corrected_query import KendraSpellCorrectedQuery
from .kendra_warning import KendraWarning


class KendraQueryResponse(BaseModel):
    QueryId: StrictStr | None = None
    ResultItems: list[KendraQueryResultItem] | None = None
    FacetResults: list[KendraFacetResult] | None = None
    TotalNumberOfResults: StrictInt | None = None
    Warnings: list[KendraWarning] | None = None
    SpellCorrectedQueries: list[KendraSpellCorrectedQuery] | None = None
    FeaturedResultsItems: list[KendraFeaturedResultsItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
