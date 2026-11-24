from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_option import RDSOption


class RDSOptionGroup(BaseModel):
    OptionGroupName: StrictStr | None = None
    OptionGroupDescription: StrictStr | None = None
    EngineName: StrictStr | None = None
    MajorEngineVersion: StrictStr | None = None
    Options: list[RDSOption] | None = None
    AllowsVpcAndNonVpcInstanceMemberships: StrictBool | None = None
    VpcId: StrictStr | None = None
    OptionGroupArn: StrictStr | None = None
    SourceOptionGroup: StrictStr | None = None
    SourceAccountId: StrictStr | None = None
    CopyTimestamp: datetime.datetime | StrictStr | None = None
    SourceRegion: StrictStr | None = None
