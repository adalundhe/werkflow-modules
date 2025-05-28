from pydantic import BaseModel, StrictStr, StrictBool



class EC2Operator(BaseModel):
    Managed: StrictBool = False
    Principal: StrictStr