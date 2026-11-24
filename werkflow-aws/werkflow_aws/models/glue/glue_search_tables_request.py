from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .glue_property_predicate import GluePropertyPredicate
from .glue_sort_criterion import GlueSortCriterion


class GlueSearchTablesRequest(BaseModel):
    CatalogId: StrictStr | None = None
    NextToken: StrictStr | None = None
    Filters: list[GluePropertyPredicate] | None = None
    SearchText: StrictStr | None = None
    SortCriteria: list[GlueSortCriterion] | None = None
    MaxResults: StrictInt | None = None
    ResourceShareType: Literal['FOREIGN', 'ALL', 'FEDERATED'] | None = None
    IncludeStatusDetails: StrictBool | None = None
