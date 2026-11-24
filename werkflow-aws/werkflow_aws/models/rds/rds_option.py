from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rdsdb_security_group_membership_model import RDSDBSecurityGroupMembershipModel
from .rds_option_setting import RDSOptionSetting
from .rds_vpc_security_group_membership_model import RDSVpcSecurityGroupMembershipModel


class RDSOption(BaseModel):
    OptionName: StrictStr | None = None
    OptionDescription: StrictStr | None = None
    Persistent: StrictBool | None = None
    Permanent: StrictBool | None = None
    Port: StrictInt | None = None
    OptionVersion: StrictStr | None = None
    OptionSettings: list[RDSOptionSetting] | None = None
    DBSecurityGroupMemberships: list[RDSDBSecurityGroupMembershipModel] | None = None
    VpcSecurityGroupMemberships: list[RDSVpcSecurityGroupMembershipModel] | None = None
