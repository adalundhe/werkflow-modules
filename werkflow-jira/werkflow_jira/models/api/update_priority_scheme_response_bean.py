from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from .priority_scheme_with_paginated_priorities_and_projects import PrioritySchemeWithPaginatedPrioritiesAndProjects
from .task_progress_bean_json_node import TaskProgressBeanJsonNode


class UpdatePrioritySchemeResponseBean(BaseModel):
    model_config = ConfigDict(extra="allow")

    priorityScheme: PrioritySchemeWithPaginatedPrioritiesAndProjects | None = None
    task: TaskProgressBeanJsonNode | None = None
