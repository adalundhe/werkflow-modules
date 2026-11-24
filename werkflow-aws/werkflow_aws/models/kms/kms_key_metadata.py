from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .kms_multi_region_configuration import KMSMultiRegionConfiguration
from .kms_xks_key_configuration_type import KMSXksKeyConfigurationType


class KMSKeyMetadata(BaseModel):
    AWSAccountId: StrictStr | None = None
    KeyId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    Enabled: StrictBool | None = None
    Description: StrictStr | None = None
    KeyUsage: StrictStr | None = None
    KeyState: StrictStr | None = None
    DeletionDate: datetime.datetime | StrictStr | None = None
    ValidTo: datetime.datetime | StrictStr | None = None
    Origin: StrictStr | None = None
    CustomKeyStoreId: StrictStr | None = None
    CloudHsmClusterId: StrictStr | None = None
    ExpirationModel: StrictStr | None = None
    KeyManager: StrictStr | None = None
    CustomerMasterKeySpec: StrictStr | None = None
    KeySpec: StrictStr | None = None
    EncryptionAlgorithms: list[StrictStr] | None = None
    SigningAlgorithms: list[StrictStr] | None = None
    KeyAgreementAlgorithms: list[StrictStr] | None = None
    EncapsulationAlgorithms: list[StrictStr] | None = None
    MultiRegion: StrictBool | None = None
    MultiRegionConfiguration: KMSMultiRegionConfiguration | None = None
    PendingDeletionWindowInDays: StrictInt | None = None
    MacAlgorithms: list[StrictStr] | None = None
    XksKeyConfiguration: KMSXksKeyConfigurationType | None = None
    CurrentKeyMaterialId: StrictStr | None = None
