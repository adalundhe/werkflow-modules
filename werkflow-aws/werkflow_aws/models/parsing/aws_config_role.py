from pydantic import BaseModel, StrictStr


class AWSConfigRole(BaseModel):
    role_name: StrictStr
    region: StrictStr
    source_profile: StrictStr
    external_id: StrictStr
    role_arn: StrictStr