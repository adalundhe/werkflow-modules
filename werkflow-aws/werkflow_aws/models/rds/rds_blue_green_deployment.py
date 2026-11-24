from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .rds_blue_green_deployment_task import RDSBlueGreenDeploymentTask
from .rds_switchover_detail import RDSSwitchoverDetail
from .rds_tag_model import RDSTagModel


class RDSBlueGreenDeployment(BaseModel):
    BlueGreenDeploymentIdentifier: StrictStr | None = None
    BlueGreenDeploymentName: StrictStr | None = None
    Source: StrictStr | None = None
    Target: StrictStr | None = None
    SwitchoverDetails: list[RDSSwitchoverDetail] | None = None
    Tasks: list[RDSBlueGreenDeploymentTask] | None = None
    Status: StrictStr | None = None
    StatusDetails: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    DeleteTime: datetime.datetime | StrictStr | None = None
    TagList: list[RDSTagModel] | None = None
