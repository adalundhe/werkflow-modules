from pydantic import BaseModel, StrictStr, StrictInt
from .credentials import Credentials
from .role_user import RoleUser


class AssumedRoleResponse(BaseModel):
    Credentials: Credentials
    AssumedRoleUser: RoleUser | None = None
    PackedPolicySize: StrictInt | None = None
    SourceIdentity: StrictStr | None = None
