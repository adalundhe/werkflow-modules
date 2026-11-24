from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_client_credentials_details import QuickSightClientCredentialsDetails


class QuickSightClientCredentialsGrantMetadata(BaseModel):
    BaseEndpoint: StrictStr
    ClientCredentialsSource: Literal['PLAIN_CREDENTIALS'] | None = None
    ClientCredentialsDetails: QuickSightClientCredentialsDetails | None = None
