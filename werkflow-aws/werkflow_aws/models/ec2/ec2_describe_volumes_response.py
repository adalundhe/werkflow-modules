from pydantic import BaseModel, StrictStr
from .ec2_volume import EC2Volume


class EC2DescribeVolumesResponse(BaseModel):
    NextToken: StrictStr | None = None
    Volumes: list[EC2Volume] | None = None