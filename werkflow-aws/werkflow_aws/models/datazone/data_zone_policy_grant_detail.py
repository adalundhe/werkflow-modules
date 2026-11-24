from __future__ import annotations
from pydantic import BaseModel
from .data_zone_add_to_project_member_pool_policy_grant_detail import DataZoneAddToProjectMemberPoolPolicyGrantDetail
from .data_zone_create_asset_type_policy_grant_detail import DataZoneCreateAssetTypePolicyGrantDetail
from .data_zone_create_domain_unit_policy_grant_detail import DataZoneCreateDomainUnitPolicyGrantDetail
from .data_zone_create_environment_profile_policy_grant_detail import DataZoneCreateEnvironmentProfilePolicyGrantDetail
from .data_zone_create_form_type_policy_grant_detail import DataZoneCreateFormTypePolicyGrantDetail
from .data_zone_create_glossary_policy_grant_detail import DataZoneCreateGlossaryPolicyGrantDetail
from .data_zone_create_project_from_project_profile_policy_grant_detail import DataZoneCreateProjectFromProjectProfilePolicyGrantDetail
from .data_zone_create_project_policy_grant_detail import DataZoneCreateProjectPolicyGrantDetail
from .data_zone_override_domain_unit_owners_policy_grant_detail import DataZoneOverrideDomainUnitOwnersPolicyGrantDetail
from .data_zone_override_project_owners_policy_grant_detail import DataZoneOverrideProjectOwnersPolicyGrantDetail
from .data_zone_unit import DataZoneUnit
from .data_zone_use_asset_type_policy_grant_detail import DataZoneUseAssetTypePolicyGrantDetail


class DataZonePolicyGrantDetail(BaseModel):
    createDomainUnit: DataZoneCreateDomainUnitPolicyGrantDetail | None = None
    overrideDomainUnitOwners: DataZoneOverrideDomainUnitOwnersPolicyGrantDetail | None = None
    addToProjectMemberPool: DataZoneAddToProjectMemberPoolPolicyGrantDetail | None = None
    overrideProjectOwners: DataZoneOverrideProjectOwnersPolicyGrantDetail | None = None
    createGlossary: DataZoneCreateGlossaryPolicyGrantDetail | None = None
    createFormType: DataZoneCreateFormTypePolicyGrantDetail | None = None
    createAssetType: DataZoneCreateAssetTypePolicyGrantDetail | None = None
    createProject: DataZoneCreateProjectPolicyGrantDetail | None = None
    createEnvironmentProfile: DataZoneCreateEnvironmentProfilePolicyGrantDetail | None = None
    delegateCreateEnvironmentProfile: DataZoneUnit | None = None
    createEnvironment: DataZoneUnit | None = None
    createEnvironmentFromBlueprint: DataZoneUnit | None = None
    createProjectFromProjectProfile: DataZoneCreateProjectFromProjectProfilePolicyGrantDetail | None = None
    useAssetType: DataZoneUseAssetTypePolicyGrantDetail | None = None
