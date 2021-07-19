#
# Created on July 19, 2021
#
# @author: Yiqin Xiong
#

import re

from ..base.parser import BaseParser
from website.utils import ConversionUtil
from website.models import DBMSCatalog
from website.types import DBMSType, knobUnitType


# TODO: 这里的TiDBParser只是复制了Mysql的parser，需要根据情况完善
# NOTE：还可参考sap hana的parser：https://github.com/cmu-db/ottertune/pull/194/commits/10bdc3d378cf7c78110702dd85e317aa875ecf17
class TidbParser(BaseParser):
    def __init__(self, dbms_obj):
        super().__init__(dbms_obj)
        self.bytes_system = (
            (1024 ** 4, 'T'),
            (1024 ** 3, 'G'),
            (1024 ** 2, 'M'),
            (1024 ** 1, 'k'),
        )
        self.time_system = None
        self.min_bytes_unit = 'k'
        self.valid_true_val = ("on", "true", "yes", '1', 'enabled')
        self.valid_false_val = ("off", "false", "no", '0', 'disabled')

    def convert_integer(self, int_value, metadata):
        # Collected knobs/metrics do not show unit, convert to int directly
        if len(str(int_value)) == 0:
            # The value collected from the database is empty
            return 0
        try:
            try:
                converted = int(int_value)
            except ValueError:
                converted = int(float(int_value))

        except ValueError:
            raise Exception('Invalid integer format for {}: {}'.format(
                metadata.name, int_value))
        return converted

    def format_integer(self, int_value, metadata):
        int_value = int(round(int_value))
        if int_value > 0 and metadata.unit == KnobUnitType.BYTES:
            int_value = ConversionUtil.get_human_readable2(
                int_value, self.bytes_system, self.min_bytes_unit)
        return int_value

    def parse_version_string(self, version_string):
        s = version_string.split('.')[0] + '.' + version_string.split('.')[1]
        return s

# class Tidb50Parser(TidbParser):
#     def __init__(self, version):
#         dbms = DBMSCatalog.objects.get(type=DBMSType.TIDB, version=version)
#         super(Tidb50Parser, self).__init__(dbms.pk)
