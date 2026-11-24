from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2PurchaseCapacityBlockRequest(BaseModel):
    CapacityBlockOfferingId: StrictStr
    InstancePlatform: Literal['Linux/UNIX', 'Red Hat Enterprise Linux', 'SUSE Linux', 'Windows', 'Windows with SQL Server', 'Windows with SQL Server Enterprise', 'Windows with SQL Server Standard', 'Windows with SQL Server Web', 'Linux with SQL Server Standard', 'Linux with SQL Server Web', 'Linux with SQL Server Enterprise', 'RHEL with SQL Server Standard', 'RHEL with SQL Server Enterprise', 'RHEL with SQL Server Web', 'RHEL with HA', 'RHEL with HA and SQL Server Standard', 'RHEL with HA and SQL Server Enterprise', 'Ubuntu Pro']
    DryRun: StrictBool | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
