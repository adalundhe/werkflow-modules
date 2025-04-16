from pydantic import BaseModel, StrictStr, StrictInt
from .policy_arn import PolicyArn
from .provided_context import ProvidedContext
from .tag import Tag


class AssumeRoleRequest(BaseModel):
    RoleArn: StrictStr
    RoleSessionName: StrictStr
    PolicyArns: list[PolicyArn] | None = None
    Policy: StrictStr | None = None
    DurationSeconds: StrictInt | None = None
    Tags: list[Tag] | None = None
    TransitiveTagKeys: list[StrictStr] | None = None
    ExternalId: StrictStr | None = None
    SerialNumber: StrictStr | None = None
    TokenCode: StrictStr | None = None
    SourceIdentity: StrictStr | None = None
    ProvidedContexts: list[ProvidedContext] | None = None