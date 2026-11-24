from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_character_set import RDSCharacterSet
from .rds_custom_db_engine_version_ami import RDSCustomDBEngineVersionAMI
from .rds_serverless_v2_features_support import RDSServerlessV2FeaturesSupport
from .rds_tag_model import RDSTagModel
from .rds_timezone import RDSTimezone
from .rds_upgrade_target import RDSUpgradeTarget


class RDSModifyCustomDBEngineVersionResponse(BaseModel):
    Engine: StrictStr | None = None
    MajorEngineVersion: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    DatabaseInstallationFilesS3BucketName: StrictStr | None = None
    DatabaseInstallationFilesS3Prefix: StrictStr | None = None
    DatabaseInstallationFiles: list[StrictStr] | None = None
    CustomDBEngineVersionManifest: StrictStr | None = None
    DBParameterGroupFamily: StrictStr | None = None
    DBEngineDescription: StrictStr | None = None
    DBEngineVersionArn: StrictStr | None = None
    DBEngineVersionDescription: StrictStr | None = None
    DefaultCharacterSet: RDSCharacterSet | None = None
    FailureReason: StrictStr | None = None
    Image: RDSCustomDBEngineVersionAMI | None = None
    DBEngineMediaType: StrictStr | None = None
    KMSKeyId: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    SupportedCharacterSets: list[RDSCharacterSet] | None = None
    SupportedNcharCharacterSets: list[RDSCharacterSet] | None = None
    ValidUpgradeTarget: list[RDSUpgradeTarget] | None = None
    SupportedTimezones: list[RDSTimezone] | None = None
    ExportableLogTypes: list[StrictStr] | None = None
    SupportsLogExportsToCloudwatchLogs: StrictBool | None = None
    SupportsReadReplica: StrictBool | None = None
    SupportedEngineModes: list[StrictStr] | None = None
    SupportedFeatureNames: list[StrictStr] | None = None
    Status: StrictStr | None = None
    SupportsParallelQuery: StrictBool | None = None
    SupportsGlobalDatabases: StrictBool | None = None
    TagList: list[RDSTagModel] | None = None
    SupportsBabelfish: StrictBool | None = None
    SupportsLimitlessDatabase: StrictBool | None = None
    SupportsCertificateRotationWithoutRestart: StrictBool | None = None
    SupportedCACertificateIdentifiers: list[StrictStr] | None = None
    SupportsLocalWriteForwarding: StrictBool | None = None
    SupportsIntegrations: StrictBool | None = None
    ServerlessV2FeaturesSupport: RDSServerlessV2FeaturesSupport | None = None
    ResponseMetadata: dict[str, Any] | None = None
