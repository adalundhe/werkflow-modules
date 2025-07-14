from pydantic import BaseModel, StrictStr


class MSKConnectivityPublicAccess(BaseModel):
    Type: StrictStr