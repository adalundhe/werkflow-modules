from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_fpga_image_state import EC2FpgaImageState
from .ec2_pci_id import EC2PciId
from .ec2_product_code import EC2ProductCode
from .ec2_tag_model import EC2TagModel


class EC2FpgaImage(BaseModel):
    FpgaImageId: StrictStr | None = None
    FpgaImageGlobalId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ShellVersion: StrictStr | None = None
    PciId: EC2PciId | None = None
    State: EC2FpgaImageState | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    OwnerId: StrictStr | None = None
    OwnerAlias: StrictStr | None = None
    ProductCodes: list[EC2ProductCode] | None = None
    Tags: list[EC2TagModel] | None = None
    Public: StrictBool | None = None
    DataRetentionSupport: StrictBool | None = None
    InstanceTypes: list[StrictStr] | None = None
