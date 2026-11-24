from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from .page_bean_priority_with_sequence import PageBeanPriorityWithSequence
from .page_bean_project_details import PageBeanProjectDetails


class PrioritySchemeWithPaginatedPrioritiesAndProjects(BaseModel):
    model_config = ConfigDict(extra="allow")

    default: StrictBool | None = None
    defaultPriorityId: StrictStr | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    isDefault: StrictBool | None = None
    name: StrictStr | None = None
    priorities: PageBeanPriorityWithSequence | None = None
    projects: PageBeanProjectDetails | None = None
    self: StrictStr | None = None
