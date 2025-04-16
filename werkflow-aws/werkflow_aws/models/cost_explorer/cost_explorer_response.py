from pydantic import BaseModel, StrictStr
from .dimension_value_attribute import DimensionValueAttribute
from .group_definition import GroupDefinition
from .result import Result


class CostExplorerResponse(BaseModel):
    NextPageToken: StrictStr | None = None
    GroupDefinitions: list[GroupDefinition] | None = None
    ResultsByTime: list[Result]
    DimensionValueAttributes: list[DimensionValueAttribute]