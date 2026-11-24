from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_direct_internet_access import SageMakerDirectInternetAccess
from .sage_maker_instance_metadata_service_configuration import SageMakerInstanceMetadataServiceConfiguration
from .sage_maker_instance_type import SageMakerInstanceType
from .sage_maker_ip_address_type import SageMakerIPAddressType
from .sage_maker_notebook_instance_accelerator_type import SageMakerNotebookInstanceAcceleratorType
from .sage_maker_notebook_instance_status import SageMakerNotebookInstanceStatus
from .sage_maker_root_access import SageMakerRootAccess


class SageMakerDescribeNotebookInstanceResponse(BaseModel):
    NotebookInstanceArn: StrictStr | None = None
    NotebookInstanceName: StrictStr | None = None
    NotebookInstanceStatus: SageMakerNotebookInstanceStatus | None = None
    FailureReason: StrictStr | None = None
    Url: StrictStr | None = None
    InstanceType: SageMakerInstanceType | None = None
    IpAddressType: SageMakerIPAddressType | None = None
    SubnetId: StrictStr | None = None
    SecurityGroups: list[StrictStr] | None = None
    RoleArn: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    LastModifiedTime: datetime.datetime | None = None
    CreationTime: datetime.datetime | None = None
    NotebookInstanceLifecycleConfigName: StrictStr | None = None
    DirectInternetAccess: SageMakerDirectInternetAccess | None = None
    VolumeSizeInGB: StrictInt | None = None
    AcceleratorTypes: list[SageMakerNotebookInstanceAcceleratorType] | None = None
    DefaultCodeRepository: StrictStr | None = None
    AdditionalCodeRepositories: list[StrictStr] | None = None
    RootAccess: SageMakerRootAccess | None = None
    PlatformIdentifier: StrictStr | None = None
    InstanceMetadataServiceConfiguration: SageMakerInstanceMetadataServiceConfiguration | None = None
