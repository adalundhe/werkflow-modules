from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .json_node import JsonNode


class TaskProgressBeanJsonNode(BaseModel):
    description: StrictStr | None = None
    elapsedRuntime: StrictInt | None = None
    finished: StrictInt | None = None
    id: StrictStr | None = None
    lastUpdate: StrictInt | None = None
    message: StrictStr | None = None
    progress: StrictInt | None = None
    result: JsonNode | None = None
    self: StrictStr | None = None
    started: StrictInt | None = None
    status: StrictStr | None = None
    submitted: StrictInt | None = None
    submittedBy: StrictInt | None = None
