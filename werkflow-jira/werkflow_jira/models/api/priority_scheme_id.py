from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .task_progress_bean_json_node import TaskProgressBeanJsonNode


class PrioritySchemeId(BaseModel):
    id: StrictStr | None = None
    task: TaskProgressBeanJsonNode | None = None
