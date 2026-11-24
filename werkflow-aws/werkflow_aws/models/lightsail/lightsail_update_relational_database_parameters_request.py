from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_relational_database_parameter import LightsailRelationalDatabaseParameter


class LightsailUpdateRelationalDatabaseParametersRequest(BaseModel):
    relationalDatabaseName: StrictStr
    parameters: list[LightsailRelationalDatabaseParameter]
