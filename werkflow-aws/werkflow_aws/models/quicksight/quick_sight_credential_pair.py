from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_source_parameters import QuickSightDataSourceParameters


class QuickSightCredentialPair(BaseModel):
    Username: StrictStr
    Password: StrictStr
    AlternateDataSourceParameters: list[QuickSightDataSourceParameters] | None = None
