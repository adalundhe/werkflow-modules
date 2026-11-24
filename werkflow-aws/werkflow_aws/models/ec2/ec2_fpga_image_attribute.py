from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_load_permission import EC2LoadPermission
from .ec2_product_code import EC2ProductCode


class EC2FpgaImageAttribute(BaseModel):
    FpgaImageId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    LoadPermissions: list[EC2LoadPermission] | None = None
    ProductCodes: list[EC2ProductCode] | None = None
