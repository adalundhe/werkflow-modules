from pydantic import BaseModel, StrictStr


class PolicyArn(BaseModel):
    arn: StrictStr