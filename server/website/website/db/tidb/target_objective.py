#
# Created on July 19, 2021
#
# @author: Yiqin Xiong
#

from website.types import DBMSType
from ..base.target_objective import (BaseThroughput, BaseUserDefinedTarget,
                                     LESS_IS_BETTER, MORE_IS_BETTER)  # pylint: disable=relative-beyond-top-level

# TODO: 只是复制了MySQL的target_objective并把innidb相关的注释掉了，需要根据TiDB具体的优化目标来修改
# NOTE：目前的优化目标都是User Defined.
#  1)99时延 2)吞吐
target_objective_list = tuple((DBMSType.TIDB, target_obj) for target_obj in [  # pylint: disable=invalid-name
    # BaseThroughput(transactions_counter=('innodb_metrics.trx_rw_commits',
    #                                      'innodb_metrics.trx_ro_commits',
    #                                      'innodb_metrics.trx_nl_ro_commits')),
    BaseUserDefinedTarget(target_name='latency_99', improvement=LESS_IS_BETTER,
                          unit='microseconds', short_unit='us'),
    BaseUserDefinedTarget(target_name='throughput', improvement=MORE_IS_BETTER,
                          unit='transactions / seconds', short_unit='txn/s')
])
