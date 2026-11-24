from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_iam_instance_profile import GuardDutyIamInstanceProfile
from .guard_duty_product_code import GuardDutyProductCode


class GuardDutyEc2Instance(BaseModel):
    AvailabilityZone: StrictStr | None = None
    ImageDescription: StrictStr | None = None
    InstanceState: StrictStr | None = None
    IamInstanceProfile: GuardDutyIamInstanceProfile | None = None
    InstanceType: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    Platform: StrictStr | None = None
    ProductCodes: list[GuardDutyProductCode] | None = None
    Ec2NetworkInterfaceUids: list[StrictStr] | None = None
