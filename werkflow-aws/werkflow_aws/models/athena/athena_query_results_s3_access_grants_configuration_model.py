from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AthenaQueryResultsS3AccessGrantsConfigurationModel(BaseModel):
    EnableS3AccessGrants: StrictBool | None = None
    CreateUserLevelPrefix: StrictBool | None = None
    AuthenticationType: StrictStr | None = None
