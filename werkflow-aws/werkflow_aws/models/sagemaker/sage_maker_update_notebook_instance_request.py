from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .sage_maker_instance_metadata_service_configuration_model import SageMakerInstanceMetadataServiceConfigurationModel


class SageMakerUpdateNotebookInstanceRequest(BaseModel):
    NotebookInstanceName: StrictStr
    InstanceType: StrictStr | None = None
    IpAddressType: Literal['ipv4', 'dualstack'] | None = None
    PlatformIdentifier: StrictStr | None = None
    RoleArn: StrictStr | None = None
    LifecycleConfigName: StrictStr | None = None
    DisassociateLifecycleConfig: StrictBool | None = None
    VolumeSizeInGB: StrictInt | None = None
    DefaultCodeRepository: StrictStr | None = None
    AdditionalCodeRepositories: list[StrictStr] | None = None
    AcceleratorTypes: list[Literal['ml.eia1.medium', 'ml.eia1.large', 'ml.eia1.xlarge', 'ml.eia2.medium', 'ml.eia2.large', 'ml.eia2.xlarge']] | None = None
    DisassociateAcceleratorTypes: StrictBool | None = None
    DisassociateDefaultCodeRepository: StrictBool | None = None
    DisassociateAdditionalCodeRepositories: StrictBool | None = None
    RootAccess: Literal['Enabled', 'Disabled'] | None = None
    InstanceMetadataServiceConfiguration: SageMakerInstanceMetadataServiceConfigurationModel | None = None
