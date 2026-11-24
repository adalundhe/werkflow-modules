from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_iam_instance_profile import GuardDutyIamInstanceProfile
from .guard_duty_network_interface import GuardDutyNetworkInterface
from .guard_duty_product_code import GuardDutyProductCode
from .guard_duty_tag import GuardDutyTag


class GuardDutyInstanceDetails(BaseModel):
    AvailabilityZone: StrictStr | None = None
    IamInstanceProfile: GuardDutyIamInstanceProfile | None = None
    ImageDescription: StrictStr | None = None
    ImageId: StrictStr | None = None
    InstanceId: StrictStr | None = None
    InstanceState: StrictStr | None = None
    InstanceType: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    LaunchTime: StrictStr | None = None
    NetworkInterfaces: list[GuardDutyNetworkInterface] | None = None
    Platform: StrictStr | None = None
    ProductCodes: list[GuardDutyProductCode] | None = None
    Tags: list[GuardDutyTag] | None = None
