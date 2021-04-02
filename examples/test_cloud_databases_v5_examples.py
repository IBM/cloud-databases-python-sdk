# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Examples for CloudDatabasesV5
"""

import os
import time

import pytest
from ibm_cloud_databases.cloud_databases_v5 import *
from ibm_cloud_sdk_core import ApiException, read_external_sources

#
# This file provides an example of how to use the Cloud Databases service.
#
# The following configuration properties are assumed to be defined:
# CLOUD_DATABASES_URL=<service base url>
# CLOUD_DATABASES_APIKEY=<IAM apikey>
# CLOUD_DATABASES_DEPLOYMENT_ID=<ID of an example deployment>
# CLOUD_DATABASES_REPLICA_ID=<ID of an example replica>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'cloud_databases.env'

cloud_databases_service = None

config = None

deployment_id = None
replica_id = None

ip_address_1 = '195.212.0.0/16'
ip_address_3 = '172.16.0.0/16'
username = 'exampleUsername'
password = 'examplePassword'
new_password = 'exampleNewPassword'
user_type = 'database'
auto_scaling_group_id = 'member'

# Variables to hold link values
task_id_link = None
backup_id_link = None
scaling_group_id_link = None

def wait_for_task(task_id):
    """Waits for a task and checks the status.

    If the task runs for more than a minute, then we'll consider it to have succeeded.

    Args:
        task_id (string): ID of the task we are waiting for
    """

    for i in range(30):
        get_task_response = cloud_databases_service.get_task(id=task_id)

        assert get_task_response.get_status_code() == 200
        get_task_response = get_task_response.get_result()
        assert get_task_response is not None

        task = get_task_response.get('task', None)
        if task is None:
            break
        else:
            status = task['status']
            if status == 'completed' or status == 'failed':
                assert status == 'completed'
                break
            elif status == 'queued' or status == 'running':
                pass
            else:
                print('status is', status)

        time.sleep(2)

##############################################################################
# Start of Examples for Service: CloudDatabasesV5
##############################################################################
# region
class TestCloudDatabasesV5Examples():
    """
    Example Test Class for CloudDatabasesV5
    """

    @classmethod
    def setup_class(cls):
        global cloud_databases_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            cloud_databases_service = CloudDatabasesV5.new_instance()

            # end-common
            assert cloud_databases_service is not None

            # Load the configuration
            global config
            config = read_external_sources(CloudDatabasesV5.DEFAULT_SERVICE_NAME)

            global deployment_id
            deployment_id = config['DEPLOYMENT_ID']

            global replica_id
            replica_id = config['REPLICA_ID']

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_add_allowlist_entry_example(self):
        """
        add_allowlist_entry request example
        """
        try:
            print('\nadd_allowlist_entry() result:')
            # begin-addAllowlistEntry

            allowlist_entry_model = AllowlistEntry(
                address=ip_address_3,
                description='Dev IP space 3',
            )

            add_allowlist_entry_response = cloud_databases_service.add_allowlist_entry(
                id=deployment_id,
                ip_address=allowlist_entry_model,
            ).get_result()

            print(json.dumps(add_allowlist_entry_response, indent=2))

            # end-addAllowlistEntry

            global task_id_link
            task_id_link = add_allowlist_entry_response['task']['id']

            wait_for_task(task_id_link)
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_allowlist_entry_example(self):
        """
        delete_allowlist_entry request example
        """
        try:
            print('\ndelete_allowlist_entry() result:')
            # begin-deleteAllowlistEntry

            delete_allowlist_entry_response = cloud_databases_service.delete_allowlist_entry(
                id=deployment_id,
                ipaddress=ip_address_3,
            ).get_result()

            print(json.dumps(delete_allowlist_entry_response, indent=2))

            # end-deleteAllowlistEntry

            global task_id_link
            task_id_link = delete_allowlist_entry_response['task']['id']

            wait_for_task(task_id_link)
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_database_user_example(self):
        """
        create_database_user request example
        """
        try:
            print('\ncreate_database_user() result:')
            # begin-createDatabaseUser

            create_database_user_request_user_model = CreateDatabaseUserRequestUser(
                username=username,
                password=password,
            )

            create_database_user_response = cloud_databases_service.create_database_user(
                id=deployment_id,
                user_type=user_type,
                user=create_database_user_request_user_model,
            ).get_result()

            print(json.dumps(create_database_user_response, indent=2))

            # end-createDatabaseUser

            global task_id_link
            task_id_link = create_database_user_response['task']['id']

            wait_for_task(task_id_link)
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_change_user_password_example(self):
        """
        change_user_password request example
        """
        try:
            print('\nchange_user_password() result:')
            # begin-changeUserPassword

            a_password_setting_user_model = APasswordSettingUser(
                password=new_password,
            )

            change_user_password_response = cloud_databases_service.change_user_password(
                id=deployment_id,
                user_type=user_type,
                username=username,
                user=a_password_setting_user_model,
            ).get_result()

            print(json.dumps(change_user_password_response, indent=2))

            # end-changeUserPassword

            global task_id_link
            task_id_link = change_user_password_response['task']['id']

            wait_for_task(task_id_link)
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_database_user_example(self):
        """
        delete_database_user request example
        """
        try:
            print('\ndelete_database_user() result:')
            # begin-deleteDatabaseUser

            delete_database_user_response = cloud_databases_service.delete_database_user(
                id=deployment_id,
                user_type=user_type,
                username=username,
            ).get_result()

            print(json.dumps(delete_database_user_response, indent=2))

            # end-deleteDatabaseUser

            global task_id_link
            task_id_link = delete_database_user_response['task']['id']

            wait_for_task(task_id_link)
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_kill_connections_example(self):
        """
        kill_connections request example
        """
        try:
            print('\nkill_connections() result:')
            # begin-killConnections

            kill_connections_response = cloud_databases_service.kill_connections(
                id=deployment_id,
            ).get_result()

            print(json.dumps(kill_connections_response, indent=2))

            # end-killConnections

            global task_id_link
            task_id_link = kill_connections_response['task']['id']

            wait_for_task(task_id_link)
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_set_allowlist_example(self):
        """
        set_allowlist request example
        """
        try:
            print('\nset_allowlist() result:')
            # begin-setAllowlist

            allowlist_entry_model = AllowlistEntry(
                address=ip_address_1,
                description='Dev IP space 1',
            )

            set_allowlist_response = cloud_databases_service.set_allowlist(
                id=deployment_id,
                ip_addresses=[allowlist_entry_model],
                if_match='exampleETag',
            ).get_result()

            print(json.dumps(set_allowlist_response, indent=2))

            # end-setAllowlist

            global task_id_link
            task_id_link = set_allowlist_response['task']['id']

            wait_for_task(task_id_link)
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_set_autoscaling_conditions_example(self):
        """
        set_autoscaling_conditions request example
        """
        try:
            print('\nset_autoscaling_conditions() result:')
            # begin-setAutoscalingConditions

            autoscaling_memory_group_memory_scalers_io_utilization_model = AutoscalingMemoryGroupMemoryScalersIoUtilization(
                enabled=True,
                over_period='5m',
                above_percent=90,
            )

            autoscaling_memory_group_memory_scalers_model = AutoscalingMemoryGroupMemoryScalers(
                io_utilization=autoscaling_memory_group_memory_scalers_io_utilization_model,
            )

            autoscaling_memory_group_memory_rate_model = AutoscalingMemoryGroupMemoryRate(
                increase_percent=10.0,
                period_seconds=300,
                limit_mb_per_member=114432,
                units='mb',
            )

            autoscaling_memory_group_memory_model = AutoscalingMemoryGroupMemory(
                scalers=autoscaling_memory_group_memory_scalers_model,
                rate=autoscaling_memory_group_memory_rate_model,
            )

            autoscaling_set_group_autoscaling_model = AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup(
                memory=autoscaling_memory_group_memory_model,
            )

            set_autoscaling_conditions_response = cloud_databases_service.set_autoscaling_conditions(
                id=deployment_id,
                group_id=auto_scaling_group_id,
                autoscaling=autoscaling_set_group_autoscaling_model,
            ).get_result()

            print(json.dumps(set_autoscaling_conditions_response, indent=2))

            # end-setAutoscalingConditions

            global task_id_link
            task_id_link = set_autoscaling_conditions_response['task']['id']

            wait_for_task(task_id_link)
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_database_configuration_example(self):
        """
        update_database_configuration request example
        """
        try:
            print('\nupdate_database_configuration() result:')
            # begin-updateDatabaseConfiguration

            set_configuration_configuration_model = SetConfigurationConfigurationPGConfiguration(
                max_connections=200,
                max_prepared_transactions=0,
                deadlock_timeout=100,
                effective_io_concurrency=1,
                max_replication_slots=10,
                max_wal_senders=12,
                shared_buffers=16,
                synchronous_commit='local',
                wal_level='hot_standby',
                archive_timeout=300,
                log_min_duration_statement=100,
            )

            update_database_configuration_response = cloud_databases_service.update_database_configuration(
                id=deployment_id,
                configuration=set_configuration_configuration_model,
            ).get_result()

            print(json.dumps(update_database_configuration_response, indent=2))

            # end-updateDatabaseConfiguration

            global task_id_link
            task_id_link = update_database_configuration_response['task']['id']

            wait_for_task(task_id_link)
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_deployables_example(self):
        """
        list_deployables request example
        """
        try:
            print('\nlist_deployables() result:')
            # begin-listDeployables

            list_deployables_response = cloud_databases_service.list_deployables().get_result()

            print(json.dumps(list_deployables_response, indent=2))

            # end-listDeployables

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_regions_example(self):
        """
        list_regions request example
        """
        try:
            print('\nlist_regions() result:')
            # begin-listRegions

            list_regions_response = cloud_databases_service.list_regions().get_result()

            print(json.dumps(list_regions_response, indent=2))

            # end-listRegions

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_deployment_info_example(self):
        """
        get_deployment_info request example
        """
        try:
            print('\nget_deployment_info() result:')
            # begin-getDeploymentInfo

            get_deployment_info_response = cloud_databases_service.get_deployment_info(
                id=deployment_id,
            ).get_result()

            print(json.dumps(get_deployment_info_response, indent=2))

            # end-getDeploymentInfo

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_remotes_example(self):
        """
        list_remotes request example
        """
        try:
            print('\nlist_remotes() result:')
            # begin-listRemotes

            list_remotes_response = cloud_databases_service.list_remotes(
                id=deployment_id,
            ).get_result()

            print(json.dumps(list_remotes_response, indent=2))

            # end-listRemotes

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_resync_replica_example(self):
        """
        resync_replica request example
        """
        try:
            print('\nresync_replica() result:')
            # begin-resyncReplica

            resync_replica_response = cloud_databases_service.resync_replica(
                id=replica_id,
            ).get_result()

            print(json.dumps(resync_replica_response, indent=2))

            # end-resyncReplica

            global task_id_link
            task_id_link = resync_replica_response['task']['id']

            wait_for_task(task_id_link)

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    @pytest.mark.skip(reason="Skip to avoid irreversible change to test environment")
    def test_set_promotion_example(self):
        """
        set_promotion request example
        """
        try:
            print('\nset_promotion() result:')
            # begin-setPromotion

            promotion = {
                'skip_initial_backup': True,
            }

            set_promotion_model = SetPromotionPromotionPromote(
                promotion=promotion,
            )

            set_promotion_response = cloud_databases_service.set_promotion(
                id=replica_id,
                promotion=set_promotion_model,
            ).get_result()

            print(json.dumps(set_promotion_response, indent=2))

            # end-setPromotion

            global task_id_link
            task_id_link = set_promotion_response['task']['id']

            wait_for_task(task_id_link)

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_deployment_tasks_example(self):
        """
        list_deployment_tasks request example
        """
        try:
            print('\nlist_deployment_tasks() result:')
            # begin-listDeploymentTasks

            tasks = cloud_databases_service.list_deployment_tasks(
                id=deployment_id,
            ).get_result()

            print(json.dumps(tasks, indent=2))

            # end-listDeploymentTasks

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_task_example(self):
        """
        get_task request example
        """
        try:
            print('\nget_task() result:')
            # begin-getTask

            get_task_response = cloud_databases_service.get_task(
                id=task_id_link,
            ).get_result()

            print(json.dumps(get_task_response, indent=2))

            # end-getTask

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_deployment_backups_example(self):
        """
        list_deployment_backups request example
        """
        try:
            print('\nlist_deployment_backups() result:')
            # begin-listDeploymentBackups

            backups = cloud_databases_service.list_deployment_backups(
                id=deployment_id,
            ).get_result()

            print(json.dumps(backups, indent=2))

            # end-listDeploymentBackups

            global backup_id_link
            backup_id_link = backups['backups'][0]['id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_backup_info_example(self):
        """
        get_backup_info request example
        """
        try:
            print('\nget_backup_info() result:')
            # begin-getBackupInfo

            get_backup_info_response = cloud_databases_service.get_backup_info(
                backup_id=backup_id_link,
            ).get_result()

            print(json.dumps(get_backup_info_response, indent=2))

            # end-getBackupInfo

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_start_ondemand_backup_example(self):
        """
        start_ondemand_backup request example
        """
        try:
            print('\nstart_ondemand_backup() result:')
            # begin-startOndemandBackup

            start_ondemand_backup_response = cloud_databases_service.start_ondemand_backup(
                id=deployment_id,
            ).get_result()

            print(json.dumps(start_ondemand_backup_response, indent=2))

            # end-startOndemandBackup

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_pit_rdata_example(self):
        """
        get_pit_rdata request example
        """
        try:
            print('\nget_pit_rdata() result:')
            # begin-getPITRdata

            point_in_time_recovery_data = cloud_databases_service.get_pit_rdata(
                id=deployment_id,
            ).get_result()

            print(json.dumps(point_in_time_recovery_data, indent=2))

            # end-getPITRdata

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_connection_example(self):
        """
        get_connection request example
        """
        try:
            print('\nget_connection() result:')
            # begin-getConnection

            connection = cloud_databases_service.get_connection(
                id=deployment_id,
                user_type=user_type,
                user_id='exampleUserID',
                endpoint_type='public',
                certificate_root='exampleCertRoot',
            ).get_result()

            print(json.dumps(connection, indent=2))

            # end-getConnection

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_complete_connection_example(self):
        """
        complete_connection request example
        """
        try:
            print('\ncomplete_connection() result:')
            # begin-completeConnection

            connection = cloud_databases_service.complete_connection(
                id=deployment_id,
                user_type=user_type,
                user_id='exampleUserID',
                endpoint_type='public',
                password='examplePassword',
                certificate_root='exampleCertRoot',
            ).get_result()

            print(json.dumps(connection, indent=2))

            # end-completeConnection

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_deployment_scaling_groups_example(self):
        """
        list_deployment_scaling_groups request example
        """
        try:
            print('\nlist_deployment_scaling_groups() result:')
            # begin-listDeploymentScalingGroups

            groups = cloud_databases_service.list_deployment_scaling_groups(
                id=deployment_id,
            ).get_result()

            print(json.dumps(groups, indent=2))

            # end-listDeploymentScalingGroups

            global scaling_group_id_link
            scaling_group_id_link = groups['groups'][0]['id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_set_deployment_scaling_group_example(self):
        """
        set_deployment_scaling_group request example
        """
        try:
            global task_id_link
            print('\nset_deployment_scaling_group() result:')
            # begin-setDeploymentScalingGroup

            set_memory_group_memory_model = SetMemoryGroupMemory(
                allocation_mb=114688,
            )

            set_deployment_scaling_group_request_model = SetDeploymentScalingGroupRequestSetMemoryGroup(
                memory=set_memory_group_memory_model,
            )

            set_deployment_scaling_group_response = cloud_databases_service.set_deployment_scaling_group(
                id=deployment_id,
                group_id=scaling_group_id_link,
                set_deployment_scaling_group_request=set_deployment_scaling_group_request_model
            ).get_result()

            print(json.dumps(set_deployment_scaling_group_response, indent=2))

            # end-setDeploymentScalingGroup

            task_id_link = set_deployment_scaling_group_response['task']['id']
            wait_for_task(task_id_link)

        except:
            pass

        set_memory_group_memory_model.allocation_mb = 114432

        try:
            set_deployment_scaling_group_response = cloud_databases_service.set_deployment_scaling_group(
                id=deployment_id,
                group_id=scaling_group_id_link,
                set_deployment_scaling_group_request=set_deployment_scaling_group_request_model
            ).get_result()

            print(json.dumps(set_deployment_scaling_group_response, indent=2))

            task_id_link = set_deployment_scaling_group_response['task']['id']

            wait_for_task(task_id_link)

        except ApiException as e:
            pytest.fail(str(e))


    @needscredentials
    def test_get_default_scaling_groups_example(self):
        """
        get_default_scaling_groups request example
        """
        try:
            print('\nget_default_scaling_groups() result:')
            # begin-getDefaultScalingGroups

            groups = cloud_databases_service.get_default_scaling_groups(
                type='postgresql',
            ).get_result()

            print(json.dumps(groups, indent=2))

            # end-getDefaultScalingGroups

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_autoscaling_conditions_example(self):
        """
        get_autoscaling_conditions request example
        """
        try:
            print('\nget_autoscaling_conditions() result:')
            # begin-getAutoscalingConditions

            autoscaling_group = cloud_databases_service.get_autoscaling_conditions(
                id=deployment_id,
                group_id=auto_scaling_group_id,
            ).get_result()

            print(json.dumps(autoscaling_group, indent=2))

            # end-getAutoscalingConditions

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_allowlist_example(self):
        """
        get_allowlist request example
        """
        try:
            print('\nget_allowlist() result:')
            # begin-getAllowlist

            allowlist = cloud_databases_service.get_allowlist(
                id=deployment_id,
            ).get_result()

            print(json.dumps(allowlist, indent=2))

            # end-getAllowlist

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: CloudDatabasesV5
##############################################################################
