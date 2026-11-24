from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_read_client_credentials_details import QuickSightReadClientCredentialsDetails


class QuickSightReadClientCredentialsGrantMetadata(BaseModel):
    BaseEndpoint: StrictStr | None = None
    ReadClientCredentialsDetails: QuickSightReadClientCredentialsDetails | None = None
    ClientCredentialsSource: StrictStr | None = None
