from pydantic import (
    BaseModel,
    StrictStr,
    StrictBool,
    StrictInt
)
from .ec2_filter import EC2Filter


class EC2DescribeVolumesQuery(BaseModel):
    VolumeIds: list[StrictStr] | None = None
    DryRun: StrictBool = False
    Filters: list[EC2Filter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None