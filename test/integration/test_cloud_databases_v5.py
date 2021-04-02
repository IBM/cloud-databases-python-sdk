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
Integration Tests for CloudDatabasesV5
"""

import os
import time

import pytest
from ibm_cloud_databases.cloud_databases_v5 import *
from ibm_cloud_sdk_core import *

# Config file name
config_file = 'cloud_databases.env'
cloud_databases_service = None
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


class TestCloudDatabasesV5():
    """
    Integration Test Class for CloudDatabasesV5
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            global cloud_databases_service

            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.cloud_databases_service = CloudDatabasesV5.new_instance()
            cloud_databases_service = cls.cloud_databases_service
            assert cls.cloud_databases_service is not None

            cls.config = read_external_sources(
                CloudDatabasesV5.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.deployment_id = cls.config['DEPLOYMENT_ID']
            cls.replica_id = cls.config['REPLICA_ID']

            assert cls.deployment_id is not None
            assert cls.replica_id is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_add_allowlist_entry(self):

        # Construct a dict representation of a AllowlistEntry model
        allowlist_entry_model = {
            'address': '172.16.0.0/16',
            'description': 'Dev IP space 3'
        }

        add_allowlist_entry_response = self.cloud_databases_service.add_allowlist_entry(
            id=self.deployment_id,
            ip_address=allowlist_entry_model,
        )

        assert add_allowlist_entry_response.get_status_code() == 202
        add_allowlist_entry_response = add_allowlist_entry_response.get_result()
        assert add_allowlist_entry_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = add_allowlist_entry_response['task']['id']

        wait_for_task(task_id_link)

    @needscredentials
    def test_delete_allowlist_entry(self):

        delete_allowlist_entry_response = self.cloud_databases_service.delete_allowlist_entry(
            id=self.deployment_id,
            ipaddress='172.16.0.0/16',
        )

        assert delete_allowlist_entry_response.get_status_code() == 202
        delete_allowlist_entry_response = delete_allowlist_entry_response.get_result()
        assert delete_allowlist_entry_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = delete_allowlist_entry_response['task']['id']

        wait_for_task(task_id_link)

    @needscredentials
    def test_create_database_user(self):

        # Construct a dict representation of a CreateDatabaseUserRequestUser model
        create_database_user_request_user_model = {
            'user_type': 'database',
            'username': 'james',
            'password': 'kickoutthe'
        }

        create_database_user_response = self.cloud_databases_service.create_database_user(
            id=self.deployment_id,
            user_type='database',
            user=create_database_user_request_user_model,
        )

        assert create_database_user_response.get_status_code() == 202
        create_database_user_response = create_database_user_response.get_result()
        assert create_database_user_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = create_database_user_response['task']['id']

        wait_for_task(task_id_link)

    @needscredentials
    def test_change_user_password(self):

        # Construct a dict representation of a APasswordSettingUser model
        a_password_setting_user_model = {
            'password': 'xyzzyyzzyx'
        }

        change_user_password_response = self.cloud_databases_service.change_user_password(
            id=self.deployment_id,
            user_type='database',
            username='james',
            user=a_password_setting_user_model
        )

        assert change_user_password_response.get_status_code() == 202
        change_user_password_response = change_user_password_response.get_result()
        assert change_user_password_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = change_user_password_response['task']['id']

        wait_for_task(task_id_link)

    @needscredentials
    def test_delete_database_user(self):

        delete_database_user_response = self.cloud_databases_service.delete_database_user(
            id=self.deployment_id,
            user_type='database',
            username='james'
        )

        assert delete_database_user_response.get_status_code() == 202
        delete_database_user_response = delete_database_user_response.get_result()
        assert delete_database_user_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = delete_database_user_response['task']['id']

        wait_for_task(task_id_link)

    @needscredentials
    def test_kill_connections(self):

        kill_connections_response = self.cloud_databases_service.kill_connections(
            id=self.deployment_id
        )

        assert kill_connections_response.get_status_code() == 202
        kill_connections_response = kill_connections_response.get_result()
        assert kill_connections_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = kill_connections_response['task']['id']

        wait_for_task(task_id_link)

    @needscredentials
    def test_set_allowlist(self):

        # Construct a dict representation of a AllowlistEntry model
        allowlist_entry_model = {
            'address': '195.212.0.0/16',
            'description': 'Dev IP space 1'
        }

        set_allowlist_response = self.cloud_databases_service.set_allowlist(
            id=self.deployment_id,
            ip_addresses=[allowlist_entry_model],
            if_match='testString'
        )

        assert set_allowlist_response.get_status_code() == 202
        set_allowlist_response = set_allowlist_response.get_result()
        assert set_allowlist_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = set_allowlist_response['task']['id']

        wait_for_task(task_id_link)

    @needscredentials
    def test_set_autoscaling_conditions(self):

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryScalersIoUtilization model
        autoscaling_memory_group_memory_scalers_io_utilization_model = {
            'enabled': True,
            'over_period': '5m',
            'above_percent': 90
        }

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryScalers model
        autoscaling_memory_group_memory_scalers_model = {
            'io_utilization': autoscaling_memory_group_memory_scalers_io_utilization_model
        }

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryRate model
        autoscaling_memory_group_memory_rate_model = {
            'increase_percent': 10.0,
            'period_seconds': 300,
            'limit_mb_per_member': 114432,
            'units': 'mb'
        }

        # Construct a dict representation of a AutoscalingMemoryGroupMemory model
        autoscaling_memory_group_memory_model = {
            'scalers': autoscaling_memory_group_memory_scalers_model,
            'rate': autoscaling_memory_group_memory_rate_model
        }

        # Construct a dict representation of a AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup model
        autoscaling_set_group_autoscaling_model = {
            'memory': autoscaling_memory_group_memory_model
        }

        set_autoscaling_conditions_response = self.cloud_databases_service.set_autoscaling_conditions(
            id=self.deployment_id,
            group_id=auto_scaling_group_id,
            autoscaling=autoscaling_memory_group_memory_model,
        )

        assert set_autoscaling_conditions_response.get_status_code() == 202
        set_autoscaling_conditions_response = set_autoscaling_conditions_response.get_result()
        assert set_autoscaling_conditions_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = set_autoscaling_conditions_response['task']['id']

        wait_for_task(task_id_link)

    @needscredentials
    def test_update_database_configuration(self):

        # Construct a dict representation of a SetConfigurationConfigurationPGConfiguration model
        set_configuration_configuration_model = {
            'max_connections': 200,
            'max_prepared_transactions': 0,
            'deadlock_timeout': 100,
            'effective_io_concurrency': 1,
            'max_replication_slots': 10,
            'max_wal_senders': 12,
            'shared_buffers': 16,
            'synchronous_commit': 'local',
            'wal_level': 'hot_standby',
            'archive_timeout': 300,
            'log_min_duration_statement': 100,
        }

        update_database_configuration_response = self.cloud_databases_service.update_database_configuration(
            id=self.deployment_id,
            configuration=set_configuration_configuration_model
        )

        assert update_database_configuration_response.get_status_code() == 200
        update_database_configuration_response = update_database_configuration_response.get_result()
        assert update_database_configuration_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = update_database_configuration_response['task']['id']

        wait_for_task(task_id_link)

    @needscredentials
    def test_list_deployables(self):

        list_deployables_response = self.cloud_databases_service.list_deployables()

        assert list_deployables_response.get_status_code() == 200
        list_deployables_response = list_deployables_response.get_result()
        assert list_deployables_response is not None

    @needscredentials
    def test_list_regions(self):

        list_regions_response = self.cloud_databases_service.list_regions()

        assert list_regions_response.get_status_code() == 200
        list_regions_response = list_regions_response.get_result()
        assert list_regions_response is not None

    @needscredentials
    def test_get_deployment_info(self):

        get_deployment_info_response = self.cloud_databases_service.get_deployment_info(
            id=self.deployment_id
        )

        assert get_deployment_info_response.get_status_code() == 200
        get_deployment_info_response = get_deployment_info_response.get_result()
        assert get_deployment_info_response is not None

    @needscredentials
    def test_list_remotes(self):

        list_remotes_response = self.cloud_databases_service.list_remotes(
            id=self.deployment_id
        )

        assert list_remotes_response.get_status_code() == 200
        list_remotes_response = list_remotes_response.get_result()
        assert list_remotes_response is not None

    @needscredentials
    def test_resync_replica(self):

        resync_replica_response = self.cloud_databases_service.resync_replica(
            id=self.replica_id
        )

        assert resync_replica_response.get_status_code() == 200
        resync_replica_response = resync_replica_response.get_result()
        assert resync_replica_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = resync_replica_response['task']['id']

        wait_for_task(task_id_link)

    @needscredentials
    @pytest.mark.skip(reason="Skip to avoid irreversible change to test environment")
    def test_set_promotion(self):

        # Construct a dict representation of a SetPromotionPromotionPromote model
        set_promotion_promotion_model = {
            'promotion': {
                'skip_initial_backup': True,
            },
        }

        set_promotion_response = self.cloud_databases_service.set_promotion(
            id=self.replica_id,
            promotion=set_promotion_promotion_model
        )

        assert set_promotion_response.get_status_code() == 200
        set_promotion_response = set_promotion_response.get_result()
        assert set_promotion_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = set_promotion_response['task']['id']

        wait_for_task(task_id_link)

    @needscredentials
    def test_list_deployment_tasks(self):

        list_deployment_tasks_response = self.cloud_databases_service.list_deployment_tasks(
            id=self.deployment_id
        )

        assert list_deployment_tasks_response.get_status_code() == 200
        tasks = list_deployment_tasks_response.get_result()
        assert tasks is not None

    @needscredentials
    def test_get_task(self):

        get_task_response = self.cloud_databases_service.get_task(
            id=task_id_link
        )

        assert get_task_response.get_status_code() == 200
        get_task_response = get_task_response.get_result()
        assert get_task_response is not None

    @needscredentials
    def test_list_deployment_backups(self):

        list_deployment_backups_response = self.cloud_databases_service.list_deployment_backups(
            id=self.deployment_id
        )

        assert list_deployment_backups_response.get_status_code() == 200
        backups = list_deployment_backups_response.get_result()
        assert backups is not None

        global backup_id_link
        backup_id_link = backups['backups'][0]['id']

    @needscredentials
    def test_get_backup_info(self):

        get_backup_info_response = self.cloud_databases_service.get_backup_info(
            backup_id=backup_id_link,
        )

        assert get_backup_info_response.get_status_code() == 200
        get_backup_info_response = get_backup_info_response.get_result()
        assert get_backup_info_response is not None

    @needscredentials
    def test_start_ondemand_backup(self):

        start_ondemand_backup_response = self.cloud_databases_service.start_ondemand_backup(
            id=self.deployment_id,
        )

        assert start_ondemand_backup_response.get_status_code() == 200
        start_ondemand_backup_response = start_ondemand_backup_response.get_result()
        assert start_ondemand_backup_response is not None

    @needscredentials
    def test_get_pit_rdata(self):

        get_pit_rdata_response = self.cloud_databases_service.get_pit_rdata(
            id=self.deployment_id,
        )

        assert get_pit_rdata_response.get_status_code() == 200
        point_in_time_recovery_data = get_pit_rdata_response.get_result()
        assert point_in_time_recovery_data is not None

    @needscredentials
    def test_get_connection(self):

        get_connection_response = self.cloud_databases_service.get_connection(
            id=self.deployment_id,
            user_type='database',
            user_id='testString',
            endpoint_type='public',
            certificate_root='testString',
        )

        assert get_connection_response.get_status_code() == 200
        connection = get_connection_response.get_result()
        assert connection is not None

    @needscredentials
    def test_complete_connection(self):

        complete_connection_response = self.cloud_databases_service.complete_connection(
            id=self.deployment_id,
            user_type='database',
            user_id='testString',
            endpoint_type='public',
            password='providedpassword',
            certificate_root='testString',
        )

        assert complete_connection_response.get_status_code() == 200
        connection = complete_connection_response.get_result()
        assert connection is not None

    @needscredentials
    def test_list_deployment_scaling_groups(self):

        list_deployment_scaling_groups_response = self.cloud_databases_service.list_deployment_scaling_groups(
            id=self.deployment_id,
        )

        assert list_deployment_scaling_groups_response.get_status_code() == 200
        groups = list_deployment_scaling_groups_response.get_result()
        assert groups is not None

        global scaling_group_id_link
        scaling_group_id_link = groups['groups'][0]['id']

    @needscredentials
    def test_set_deployment_scaling_group(self):

        global task_id_link

        # Construct a dict representation of a SetMemoryGroupMemory model
        set_memory_group_memory_model = {
            'allocation_mb': 114688
        }

        # Construct a dict representation of a SetDeploymentScalingGroupRequestSetMemoryGroup model
        set_deployment_scaling_group_request_model = {
            'memory': set_memory_group_memory_model
        }

        # set_deployment_scaling_group will fail if the value sent matches the current value.
        # So first we make a request to set to one value -- and that might fail but we don't care
        # Then we'll make a request to set to a different value, and that one we will check for success
        try:
            set_deployment_scaling_group_response = self.cloud_databases_service.set_deployment_scaling_group(
                id=self.deployment_id,
                group_id=scaling_group_id_link,
                set_deployment_scaling_group_request=set_deployment_scaling_group_request_model,
            )

            task_id_link = set_deployment_scaling_group_response['task']['id']
            wait_for_task(task_id_link)
        except:
            pass

        set_memory_group_memory_model['allocation_mb'] = 114432

        set_deployment_scaling_group_response = self.cloud_databases_service.set_deployment_scaling_group(
            id=self.deployment_id,
            group_id=scaling_group_id_link,
            set_deployment_scaling_group_request=set_deployment_scaling_group_request_model,
        )

        assert set_deployment_scaling_group_response.get_status_code() == 202
        set_deployment_scaling_group_response = set_deployment_scaling_group_response.get_result()
        assert set_deployment_scaling_group_response is not None

        # Store task_id_link value for later test cases
        task_id_link = set_deployment_scaling_group_response['task']['id']

        wait_for_task(task_id_link)

    @needscredentials
    def test_get_default_scaling_groups(self):

        get_default_scaling_groups_response = self.cloud_databases_service.get_default_scaling_groups(
            type='postgresql'
        )

        assert get_default_scaling_groups_response.get_status_code() == 200
        groups = get_default_scaling_groups_response.get_result()
        assert groups is not None

    @needscredentials
    def test_get_autoscaling_conditions(self):

        get_autoscaling_conditions_response = self.cloud_databases_service.get_autoscaling_conditions(
            id=self.deployment_id,
            group_id=auto_scaling_group_id
        )

        assert get_autoscaling_conditions_response.get_status_code() == 200
        autoscaling_group = get_autoscaling_conditions_response.get_result()
        assert autoscaling_group is not None

    @needscredentials
    def test_get_allowlist(self):

        get_allowlist_response = self.cloud_databases_service.get_allowlist(
            id=self.deployment_id
        )

        assert get_allowlist_response.get_status_code() == 200
        allowlist = get_allowlist_response.get_result()
        assert allowlist is not None
