from pydantic import BaseModel, StrictBool


class MSKNodeExporter(BaseModel):
    EnabledInBroker: StrictBool = False