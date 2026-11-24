from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_capacity_allocation import EC2CapacityAllocation
from .ec2_capacity_reservation_adjustment_details import EC2CapacityReservationAdjustmentDetails
from .ec2_capacity_reservation_commitment_info import EC2CapacityReservationCommitmentInfo
from .ec2_interruptible_capacity_allocation import EC2InterruptibleCapacityAllocation
from .ec2_interruption_info import EC2InterruptionInfo
from .ec2_tag_model import EC2TagModel


class EC2CapacityReservation(BaseModel):
    CapacityReservationId: StrictStr | None = None
    OwnerId: StrictStr | None = None
    CapacityReservationArn: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    InstancePlatform: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    Tenancy: StrictStr | None = None
    TotalInstanceCount: StrictInt | None = None
    AvailableInstanceCount: StrictInt | None = None
    EbsOptimized: StrictBool | None = None
    EphemeralStorage: StrictBool | None = None
    State: StrictStr | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    EndDateType: StrictStr | None = None
    InstanceMatchCriteria: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    OutpostArn: StrictStr | None = None
    CapacityReservationFleetId: StrictStr | None = None
    PlacementGroupArn: StrictStr | None = None
    CapacityAllocations: list[EC2CapacityAllocation] | None = None
    ReservationType: StrictStr | None = None
    UnusedReservationBillingOwnerId: StrictStr | None = None
    CommitmentInfo: EC2CapacityReservationCommitmentInfo | None = None
    DeliveryPreference: StrictStr | None = None
    CapacityBlockId: StrictStr | None = None
    Interruptible: StrictBool | None = None
    InterruptibleCapacityAllocation: EC2InterruptibleCapacityAllocation | None = None
    InterruptionInfo: EC2InterruptionInfo | None = None
    AdjustmentStatus: StrictStr | None = None
    AdjustmentDetails: EC2CapacityReservationAdjustmentDetails | None = None
    OriginalStartDate: datetime.datetime | StrictStr | None = None
    ZeroSizePreference: StrictStr | None = None
    LaunchStatus: StrictStr | None = None
