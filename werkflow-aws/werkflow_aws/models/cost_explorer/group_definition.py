from pydantic import BaseModel, StrictStr
from typing import Literal


GroupTypes = Literal[
    "DIMENSION",
    "TAG",
    "COST_CATEGORY"
]


class GroupDefinition(BaseModel):
    Type: GroupTypes
    Key: StrictStr