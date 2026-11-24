from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WorkSpacesModifyEndpointEncryptionModeRequest(BaseModel):
    DirectoryId: StrictStr
    EndpointEncryptionMode: Literal['STANDARD_TLS', 'FIPS_VALIDATED']
