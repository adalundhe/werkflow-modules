from pydantic import BaseModel, StrictStr
from .group_definition import GroupDefinition
from .result import Result


class CostExplorerResponse(BaseModel):
    NextPageToken: StrictStr
    GroupDefinitions: list[GroupDefinition] | None = None
    ResultsByTime: list[Result]
    