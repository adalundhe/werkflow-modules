from pydantic import BaseModel, StrictInt, StrictStr
from .policy_arn import PolicyArn


class AssumeRoleWithWebIdentityRequest(BaseModel):
    RoleArn: StrictStr
    RoleSessionName: StrictStr
    WebIdentityToken: StrictStr
    ProviderId: StrictStr | None = None
    PolicyArns: list[PolicyArn] | None = None
    Policy: StrictStr | None = None
    DurationSeconds: StrictInt | None = None
