from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .json_node import JsonNode


class IssueEntityPropertiesForMultiUpdate(BaseModel):
    issueID: StrictInt | None = None
    properties: dict[StrictStr, JsonNode] | None = None
