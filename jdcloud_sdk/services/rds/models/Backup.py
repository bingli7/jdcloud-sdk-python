# coding=utf8

# Copyright 2018-2025 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class Backup(object):

    def __init__(self, backupId=None, backupName=None, instanceId=None, backupStatus=None, backupStartTime=None, backupEndTime=None, backupType=None, backupMode=None, backupUnit=None, backupFiles=None, backupSizeByte=None):
        """
        :param backupId: (Optional) 备份ID
        :param backupName: (Optional) 备份名称
        :param instanceId: (Optional) 备份所属实例ID
        :param backupStatus: (Optional) 备份状态，COMPLETED：备份完成，FAILED：备份失败，BUILDING：备份中，DELETING：删除中
        :param backupStartTime: (Optional) 备份开始时间，遵循ISO8601标准，使用UTC时间，格式为：YYYY-MM-DDTHH:mm:ssZ
        :param backupEndTime: (Optional) 备份结束时间，遵循ISO8601标准，使用UTC时间，格式为：YYYY-MM-DDTHH:mm:ssZ
        :param backupType: (Optional) 备份类型，全量备份或增量备份，full：全量，diff：增量
        :param backupMode: (Optional) 备份模式，系统自动备份或手动备份，Automated：自动备份  Manual：手工备份
        :param backupUnit: (Optional) 备份粒度，实例备份或者多库备份，instance：实例备份 ，dbs：数据库备份
        :param backupFiles: (Optional) 备份文件列表，仅SQL Server支持该参数，文件名的命名规则为:全备:数据库名+.bak; 增量:数据库名+.diff
        :param backupSizeByte: (Optional) 整个备份集大小，单位：Byte
        """

        self.backupId = backupId
        self.backupName = backupName
        self.instanceId = instanceId
        self.backupStatus = backupStatus
        self.backupStartTime = backupStartTime
        self.backupEndTime = backupEndTime
        self.backupType = backupType
        self.backupMode = backupMode
        self.backupUnit = backupUnit
        self.backupFiles = backupFiles
        self.backupSizeByte = backupSizeByte