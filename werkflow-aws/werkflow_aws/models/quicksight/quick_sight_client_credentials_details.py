from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_client_credentials_grant_details import QuickSightClientCredentialsGrantDetails


class QuickSightClientCredentialsDetails(BaseModel):
    ClientCredentialsGrantDetails: QuickSightClientCredentialsGrantDetails | None = None
