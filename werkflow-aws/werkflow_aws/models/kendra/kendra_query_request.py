from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .kendra_attribute_filter import KendraAttributeFilter
from .kendra_collapse_configuration import KendraCollapseConfiguration
from .kendra_document_relevance_configuration import KendraDocumentRelevanceConfiguration
from .kendra_facet import KendraFacet
from .kendra_sorting_configuration import KendraSortingConfiguration
from .kendra_spell_correction_configuration import KendraSpellCorrectionConfiguration
from .kendra_user_context import KendraUserContext


class KendraQueryRequest(BaseModel):
    IndexId: StrictStr
    QueryText: StrictStr | None = None
    AttributeFilter: KendraAttributeFilter | None = None
    Facets: list[KendraFacet] | None = None
    RequestedDocumentAttributes: list[StrictStr] | None = None
    QueryResultTypeFilter: Literal['DOCUMENT', 'QUESTION_ANSWER', 'ANSWER'] | None = None
    DocumentRelevanceOverrideConfigurations: list[KendraDocumentRelevanceConfiguration] | None = None
    PageNumber: StrictInt | None = None
    PageSize: StrictInt | None = None
    SortingConfiguration: KendraSortingConfiguration | None = None
    SortingConfigurations: list[KendraSortingConfiguration] | None = None
    UserContext: KendraUserContext | None = None
    VisitorId: StrictStr | None = None
    SpellCorrectionConfiguration: KendraSpellCorrectionConfiguration | None = None
    CollapseConfiguration: KendraCollapseConfiguration | None = None
