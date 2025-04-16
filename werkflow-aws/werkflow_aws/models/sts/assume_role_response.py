from pydantic import BaseModel, StrictStr, StrictInt
from .credentials import Credentials
from .assumed_role_user import AssumedRoleUser


class AssumedRoleResponse(BaseModel):
    Credentials: Credentials
    AssumedRoledUser: AssumedRoleUser | None = None
    PackedPolicySize: StrictInt | None = None
    SourceIdentity: StrictStr | None = None
