from pydantic import BaseModel, StrictStr, StrictInt
from .credentials import Credentials
from .assumed_role_user import AssumedRoledUser


class AssumedRoleResponse(BaseModel):
    Credentials: Credentials
    AssumedRoledUser: AssumedRoledUser
    PackedPolicySize: StrictInt
    SourceIdentity: StrictStr
