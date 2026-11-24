from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class LightsailClient(ABC):

    @abstractmethod
    def allocate_static_ip(
        self,
        *,
        staticIpName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_certificate_to_distribution(
        self,
        *,
        distributionName: str,
        certificateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_disk(
        self,
        *,
        diskName: str,
        instanceName: str,
        diskPath: str,
        autoMounting: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_instances_to_load_balancer(
        self,
        *,
        loadBalancerName: str,
        instanceNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_load_balancer_tls_certificate(
        self,
        *,
        loadBalancerName: str,
        certificateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_static_ip(
        self,
        *,
        staticIpName: str,
        instanceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def check_subdomain_availability(
        self,
        *,
        subdomainName: str,
        reserve: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def close_instance_public_ports(
        self,
        *,
        portInfo: dict[str, Any],
        instanceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_snapshot(
        self,
        *,
        targetSnapshotName: str,
        sourceRegion: str,
        sourceSnapshotName: str | None = None,
        sourceResourceName: str | None = None,
        restoreDate: str | None = None,
        useLatestRestorableAutoSnapshot: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_bucket(
        self,
        *,
        bucketName: str,
        bundleId: str,
        tags: list[dict[str, Any]] | None = None,
        enableObjectVersioning: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_bucket_access_key(
        self,
        *,
        bucketName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_certificate(
        self,
        *,
        certificateName: str,
        domainName: str,
        subjectAlternativeNames: list[str] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cloud_formation_stack(
        self,
        *,
        instances: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_contact_method(
        self,
        *,
        protocol: str,
        contactEndpoint: str,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_container_service(
        self,
        *,
        serviceName: str,
        power: str,
        scale: int,
        tags: list[dict[str, Any]] | None = None,
        publicDomainNames: dict[str, list[str]] | None = None,
        deployment: dict[str, Any] | None = None,
        privateRegistryAccess: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_container_service_deployment(
        self,
        *,
        serviceName: str,
        containers: dict[str, dict[str, Any]] | None = None,
        publicEndpoint: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_container_service_registry_login(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_disk(
        self,
        *,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        tags: list[dict[str, Any]] | None = None,
        addOns: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_disk_from_snapshot(
        self,
        *,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        diskSnapshotName: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        addOns: list[dict[str, Any]] | None = None,
        sourceDiskName: str | None = None,
        restoreDate: str | None = None,
        useLatestRestorableAutoSnapshot: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_disk_snapshot(
        self,
        *,
        diskSnapshotName: str,
        diskName: str | None = None,
        instanceName: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_distribution(
        self,
        *,
        distributionName: str,
        origin: dict[str, Any],
        defaultCacheBehavior: dict[str, Any],
        bundleId: str,
        cacheBehaviorSettings: dict[str, Any] | None = None,
        cacheBehaviors: list[dict[str, Any]] | None = None,
        ipAddressType: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        certificateName: str | None = None,
        viewerMinimumTlsProtocolVersion: str | None = None,
        enablePrivateOriginAccess: bool | None = None,
        defaultRootObject: str | None = None,
        customErrorResponses: list[dict[str, Any]] | None = None,
        enableWaf: bool | None = None,
        wafRules: list[dict[str, Any]] | None = None,
        subdomainName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain(
        self,
        *,
        domainName: str,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain_entry(
        self,
        *,
        domainName: str,
        domainEntry: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_gui_session_access_details(
        self,
        *,
        resourceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_instance_snapshot(
        self,
        *,
        instanceSnapshotName: str,
        instanceName: str,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_instances(
        self,
        *,
        instanceNames: list[str],
        availabilityZone: str,
        blueprintId: str,
        bundleId: str,
        customImageName: str | None = None,
        userData: str | None = None,
        keyPairName: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        addOns: list[dict[str, Any]] | None = None,
        ipAddressType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_instances_from_snapshot(
        self,
        *,
        instanceNames: list[str],
        availabilityZone: str,
        bundleId: str,
        attachedDiskMapping: dict[str, list[dict[str, Any]]] | None = None,
        instanceSnapshotName: str | None = None,
        userData: str | None = None,
        keyPairName: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        addOns: list[dict[str, Any]] | None = None,
        ipAddressType: str | None = None,
        sourceInstanceName: str | None = None,
        restoreDate: str | None = None,
        useLatestRestorableAutoSnapshot: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_key_pair(
        self,
        *,
        keyPairName: str,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_load_balancer(
        self,
        *,
        loadBalancerName: str,
        instancePort: int,
        healthCheckPath: str | None = None,
        certificateName: str | None = None,
        certificateDomainName: str | None = None,
        certificateAlternativeNames: list[str] | None = None,
        tags: list[dict[str, Any]] | None = None,
        ipAddressType: str | None = None,
        tlsPolicyName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_load_balancer_tls_certificate(
        self,
        *,
        loadBalancerName: str,
        certificateName: str,
        certificateDomainName: str,
        certificateAlternativeNames: list[str] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_relational_database(
        self,
        *,
        relationalDatabaseName: str,
        relationalDatabaseBlueprintId: str,
        relationalDatabaseBundleId: str,
        masterDatabaseName: str,
        masterUsername: str,
        availabilityZone: str | None = None,
        masterUserPassword: str | None = None,
        preferredBackupWindow: str | None = None,
        preferredMaintenanceWindow: str | None = None,
        publiclyAccessible: bool | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_relational_database_from_snapshot(
        self,
        *,
        relationalDatabaseName: str,
        availabilityZone: str | None = None,
        publiclyAccessible: bool | None = None,
        relationalDatabaseSnapshotName: str | None = None,
        relationalDatabaseBundleId: str | None = None,
        sourceRelationalDatabaseName: str | None = None,
        restoreTime: datetime.datetime | str | None = None,
        useLatestRestorableTime: bool | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_relational_database_snapshot(
        self,
        *,
        relationalDatabaseName: str,
        relationalDatabaseSnapshotName: str,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_subdomain(
        self,
        *,
        subdomainName: str,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_alarm(
        self,
        *,
        alarmName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_auto_snapshot(
        self,
        *,
        resourceName: str,
        date: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket(
        self,
        *,
        bucketName: str,
        forceDelete: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_bucket_access_key(
        self,
        *,
        bucketName: str,
        accessKeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_certificate(
        self,
        *,
        certificateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_contact_method(
        self,
        *,
        protocol: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_container_image(
        self,
        *,
        serviceName: str,
        image: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_container_service(
        self,
        *,
        serviceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_disk(
        self,
        *,
        diskName: str,
        forceDeleteAddOns: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_disk_snapshot(
        self,
        *,
        diskSnapshotName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_distribution(
        self,
        *,
        distributionName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain(
        self,
        *,
        domainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain_entry(
        self,
        *,
        domainName: str,
        domainEntry: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_instance(
        self,
        *,
        instanceName: str,
        forceDeleteAddOns: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_instance_snapshot(
        self,
        *,
        instanceSnapshotName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_key_pair(
        self,
        *,
        keyPairName: str,
        expectedFingerprint: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_known_host_keys(
        self,
        *,
        instanceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_load_balancer(
        self,
        *,
        loadBalancerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_load_balancer_tls_certificate(
        self,
        *,
        loadBalancerName: str,
        certificateName: str,
        force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_relational_database(
        self,
        *,
        relationalDatabaseName: str,
        skipFinalSnapshot: bool | None = None,
        finalRelationalDatabaseSnapshotName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_relational_database_snapshot(
        self,
        *,
        relationalDatabaseSnapshotName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_subdomain(
        self,
        *,
        subdomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_certificate_from_distribution(
        self,
        *,
        distributionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_disk(
        self,
        *,
        diskName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_instances_from_load_balancer(
        self,
        *,
        loadBalancerName: str,
        instanceNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_static_ip(
        self,
        *,
        staticIpName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_add_on(
        self,
        *,
        addOnType: str,
        resourceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def download_default_key_pair(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_add_on(
        self,
        *,
        resourceName: str,
        addOnRequest: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_snapshot(
        self,
        *,
        sourceSnapshotName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_active_names(
        self,
        *,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_alarms(
        self,
        *,
        alarmName: str | None = None,
        pageToken: str | None = None,
        monitoredResourceName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_auto_snapshots(
        self,
        *,
        resourceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_blueprints(
        self,
        *,
        includeInactive: bool | None = None,
        pageToken: str | None = None,
        appCategory: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_access_keys(
        self,
        *,
        bucketName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_bundles(
        self,
        *,
        includeInactive: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bucket_metric_data(
        self,
        *,
        bucketName: str,
        metricName: str,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
        period: int,
        statistics: list[str],
        unit: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_buckets(
        self,
        *,
        bucketName: str | None = None,
        pageToken: str | None = None,
        includeConnectedResources: bool | None = None,
        includeCors: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bundles(
        self,
        *,
        includeInactive: bool | None = None,
        pageToken: str | None = None,
        appCategory: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_certificates(
        self,
        *,
        certificateStatuses: list[str] | None = None,
        includeCertificateDetails: bool | None = None,
        certificateName: str | None = None,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cloud_formation_stack_records(
        self,
        *,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_contact_methods(
        self,
        *,
        protocols: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_container_api_metadata(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_container_images(
        self,
        *,
        serviceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_container_log(
        self,
        *,
        serviceName: str,
        containerName: str,
        startTime: datetime.datetime | str | None = None,
        endTime: datetime.datetime | str | None = None,
        filterPattern: str | None = None,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_container_service_deployments(
        self,
        *,
        serviceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_container_service_metric_data(
        self,
        *,
        serviceName: str,
        metricName: str,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
        period: int,
        statistics: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_container_service_powers(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_container_services(
        self,
        *,
        serviceName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cost_estimate(
        self,
        *,
        resourceName: str,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_disk(
        self,
        *,
        diskName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_disk_snapshot(
        self,
        *,
        diskSnapshotName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_disk_snapshots(
        self,
        *,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_disks(
        self,
        *,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_distribution_bundles(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_distribution_latest_cache_reset(
        self,
        *,
        distributionName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_distribution_metric_data(
        self,
        *,
        distributionName: str,
        metricName: str,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
        period: int,
        unit: str,
        statistics: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_distributions(
        self,
        *,
        distributionName: str | None = None,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain(
        self,
        *,
        domainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domains(
        self,
        *,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_export_snapshot_records(
        self,
        *,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_instance(
        self,
        *,
        instanceName: str,
        includeHealthStatus: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_instance_access_details(
        self,
        *,
        instanceName: str,
        protocol: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_instance_metric_data(
        self,
        *,
        instanceName: str,
        metricName: str,
        period: int,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
        unit: str,
        statistics: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_instance_port_states(
        self,
        *,
        instanceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_instance_snapshot(
        self,
        *,
        instanceSnapshotName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_instance_snapshots(
        self,
        *,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_instance_state(
        self,
        *,
        instanceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_instances(
        self,
        *,
        pageToken: str | None = None,
        includeHealthStatus: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_key_pair(
        self,
        *,
        keyPairName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_key_pairs(
        self,
        *,
        pageToken: str | None = None,
        includeDefaultKeyPair: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_load_balancer(
        self,
        *,
        loadBalancerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_load_balancer_metric_data(
        self,
        *,
        loadBalancerName: str,
        metricName: str,
        period: int,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
        unit: str,
        statistics: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_load_balancer_tls_certificates(
        self,
        *,
        loadBalancerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_load_balancer_tls_policies(
        self,
        *,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_load_balancers(
        self,
        *,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_operation(
        self,
        *,
        operationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_operations(
        self,
        *,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_operations_for_resource(
        self,
        *,
        resourceName: str,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_profile(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_regions(
        self,
        *,
        includeAvailabilityZones: bool | None = None,
        includeRelationalDatabaseAvailabilityZones: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_relational_database(
        self,
        *,
        relationalDatabaseName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_relational_database_blueprints(
        self,
        *,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_relational_database_bundles(
        self,
        *,
        pageToken: str | None = None,
        includeInactive: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_relational_database_events(
        self,
        *,
        relationalDatabaseName: str,
        durationInMinutes: int | None = None,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_relational_database_log_events(
        self,
        *,
        relationalDatabaseName: str,
        logStreamName: str,
        startTime: datetime.datetime | str | None = None,
        endTime: datetime.datetime | str | None = None,
        startFromHead: bool | None = None,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_relational_database_log_streams(
        self,
        *,
        relationalDatabaseName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_relational_database_master_user_password(
        self,
        *,
        relationalDatabaseName: str,
        passwordVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_relational_database_metric_data(
        self,
        *,
        relationalDatabaseName: str,
        metricName: str,
        period: int,
        startTime: datetime.datetime | str,
        endTime: datetime.datetime | str,
        unit: str,
        statistics: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_relational_database_parameters(
        self,
        *,
        relationalDatabaseName: str,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_relational_database_snapshot(
        self,
        *,
        relationalDatabaseSnapshotName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_relational_database_snapshots(
        self,
        *,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_relational_databases(
        self,
        *,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_setup_history(
        self,
        *,
        resourceName: str,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_static_ip(
        self,
        *,
        staticIpName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_static_ips(
        self,
        *,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_subdomains(
        self,
        *,
        subdomainName: str | None = None,
        pageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_key_pair(
        self,
        *,
        keyPairName: str,
        publicKeyBase64: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def is_vpc_peered(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def open_instance_public_ports(
        self,
        *,
        portInfo: dict[str, Any],
        instanceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def peer_vpc(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_alarm(
        self,
        *,
        alarmName: str,
        metricName: str,
        monitoredResourceName: str,
        comparisonOperator: str,
        threshold: float | int,
        evaluationPeriods: int,
        datapointsToAlarm: int | None = None,
        treatMissingData: str | None = None,
        contactProtocols: list[str] | None = None,
        notificationTriggers: list[str] | None = None,
        notificationEnabled: bool | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_instance_public_ports(
        self,
        *,
        portInfos: list[dict[str, Any]],
        instanceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reboot_instance(
        self,
        *,
        instanceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reboot_relational_database(
        self,
        *,
        relationalDatabaseName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_container_image(
        self,
        *,
        serviceName: str,
        label: str,
        digest: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def release_static_ip(
        self,
        *,
        staticIpName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_distribution_cache(
        self,
        *,
        distributionName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_contact_method_verification(
        self,
        *,
        protocol: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_ip_address_type(
        self,
        *,
        resourceType: str,
        resourceName: str,
        ipAddressType: str,
        acceptBundleUpdate: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_resource_access_for_bucket(
        self,
        *,
        resourceName: str,
        bucketName: str,
        access: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def setup_instance_https(
        self,
        *,
        instanceName: str,
        emailAddress: str,
        domainNames: list[str],
        certificateProvider: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_gui_session(
        self,
        *,
        resourceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_instance(
        self,
        *,
        instanceName: str,
        attributeUpdates: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_relational_database(
        self,
        *,
        relationalDatabaseName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_gui_session(
        self,
        *,
        resourceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_instance(
        self,
        *,
        instanceName: str,
        force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_relational_database(
        self,
        *,
        relationalDatabaseName: str,
        relationalDatabaseSnapshotName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceName: str,
        tags: list[dict[str, Any]],
        resourceArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_alarm(
        self,
        *,
        alarmName: str,
        state: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def unpeer_vpc(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceName: str,
        tagKeys: list[str],
        resourceArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_bucket(
        self,
        *,
        bucketName: str,
        accessRules: dict[str, Any] | None = None,
        versioning: str | None = None,
        readonlyAccessAccounts: list[str] | None = None,
        accessLogConfig: dict[str, Any] | None = None,
        cors: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_bucket_bundle(
        self,
        *,
        bucketName: str,
        bundleId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_container_service(
        self,
        *,
        serviceName: str,
        power: str | None = None,
        scale: int | None = None,
        isDisabled: bool | None = None,
        publicDomainNames: dict[str, list[str]] | None = None,
        privateRegistryAccess: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_distribution(
        self,
        *,
        distributionName: str,
        origin: dict[str, Any] | None = None,
        defaultCacheBehavior: dict[str, Any] | None = None,
        cacheBehaviorSettings: dict[str, Any] | None = None,
        cacheBehaviors: list[dict[str, Any]] | None = None,
        isEnabled: bool | None = None,
        viewerMinimumTlsProtocolVersion: str | None = None,
        certificateName: str | None = None,
        useDefaultCertificate: bool | None = None,
        enablePrivateOriginAccess: bool | None = None,
        defaultRootObject: str | None = None,
        customErrorResponses: list[dict[str, Any]] | None = None,
        enableWaf: bool | None = None,
        wafRules: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_distribution_bundle(
        self,
        *,
        distributionName: str | None = None,
        bundleId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain_entry(
        self,
        *,
        domainName: str,
        domainEntry: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_instance_metadata_options(
        self,
        *,
        instanceName: str,
        httpTokens: str | None = None,
        httpEndpoint: str | None = None,
        httpPutResponseHopLimit: int | None = None,
        httpProtocolIpv6: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_load_balancer_attribute(
        self,
        *,
        loadBalancerName: str,
        attributeName: str,
        attributeValue: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_relational_database(
        self,
        *,
        relationalDatabaseName: str,
        masterUserPassword: str | None = None,
        rotateMasterUserPassword: bool | None = None,
        preferredBackupWindow: str | None = None,
        preferredMaintenanceWindow: str | None = None,
        enableBackupRetention: bool | None = None,
        disableBackupRetention: bool | None = None,
        publiclyAccessible: bool | None = None,
        applyImmediately: bool | None = None,
        caCertificateIdentifier: str | None = None,
        relationalDatabaseBlueprintId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_relational_database_parameters(
        self,
        *,
        relationalDatabaseName: str,
        parameters: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_subdomain_association(
        self,
        *,
        subdomainName: str,
        action: str,
        targetResourceArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
