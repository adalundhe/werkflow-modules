from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .priority_mapping import PriorityMapping
from .update_priorities_in_scheme_request_bean import UpdatePrioritiesInSchemeRequestBean
from .update_projects_in_scheme_request_bean import UpdateProjectsInSchemeRequestBean


class UpdatePrioritySchemeRequestBean(BaseModel):
    defaultPriorityId: StrictInt | None = None
    description: StrictStr | None = None
    mappings: PriorityMapping | None = None
    name: StrictStr | None = None
    priorities: UpdatePrioritiesInSchemeRequestBean | None = None
    projects: UpdateProjectsInSchemeRequestBean | None = None
