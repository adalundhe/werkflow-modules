from pydantic import (
    BaseModel,
    StrictBool,
    StrictStr,
)


class AthenaQueryResultsS3AccessGrantsConfiguration(BaseModel):
    EnableS3AccessGrants: StrictBool = False
    CreateUserLevelPrefix: StrictBool = False
    AuthenticationType: StrictStr