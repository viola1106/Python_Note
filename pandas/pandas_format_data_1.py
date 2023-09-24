import re
from datetime import datetime
from glob import glob
from os import getcwd

import pandas as pd

main_dir = '\\'.join(getcwd().split('\\')) # 當前路徑
test_file = pd.read_excel(f"{main_dir}\\format_data_1.xlsx", sheet_name='test').fillna('')  # test_file



