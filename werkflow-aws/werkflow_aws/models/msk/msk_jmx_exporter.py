from pydantic import BaseModel, StrictBool


class MSKJmxExporter(BaseModel):
    EnabledInBroker: StrictBool = False