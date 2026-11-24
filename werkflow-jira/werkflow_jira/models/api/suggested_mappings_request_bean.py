from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .suggested_mappings_for_priorities_request_bean import SuggestedMappingsForPrioritiesRequestBean
from .suggested_mappings_for_projects_request_bean import SuggestedMappingsForProjectsRequestBean


class SuggestedMappingsRequestBean(BaseModel):
    maxResults: StrictInt | None = None
    priorities: SuggestedMappingsForPrioritiesRequestBean | None = None
    projects: SuggestedMappingsForProjectsRequestBean | None = None
    schemeId: StrictInt | None = None
    startAt: StrictInt | None = None
