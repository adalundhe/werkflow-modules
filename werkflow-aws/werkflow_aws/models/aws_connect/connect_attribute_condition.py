from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .connect_match_criteria import ConnectMatchCriteria
from .connect_range import ConnectRange


class ConnectAttributeCondition(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
    ProficiencyLevel: StrictFloat | StrictInt | None = None
    Range: ConnectRange | None = None
    MatchCriteria: ConnectMatchCriteria | None = None
    ComparisonOperator: StrictStr | None = None
