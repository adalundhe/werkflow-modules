from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeFpgaImagesRequest(BaseModel):
    DryRun: StrictBool | None = None
    FpgaImageIds: list[StrictStr] | None = None
    Owners: list[StrictStr] | None = None
    Filters: list[EC2FilterModel] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
