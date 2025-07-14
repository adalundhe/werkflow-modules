from pydantic import BaseModel, StrictStr


class MSKCluster(BaseModel):
    ActiveOperationArn: StrictStr