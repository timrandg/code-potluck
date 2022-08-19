import yolo  #only imported because coverage expects it to be
import subprocess
import pytest

# 1. create a new commandline tool 
# file: playground/yolo.py
# python playground/yolo.py 
# yolo
# yolo
# python playground/yolo.py --count 4
# yolo
# yolo
# yolo
# yolo
#HINT: @click.option('--flag_name', default=v, help='Number of yolos')
@pytest.mark.parametrize('c,t', [(1,1),(2,2),(3,3),(None,2)])
def test_yolo_prints_yolo_based_on_count_flag_respects_default(c,t):
    if c:
        cmd = f'python playground/yolo.py --count {c}'
    else:
        cmd = f'python playground/yolo.py'

    output = subprocess.check_output(cmd, shell=True).decode()
    assert output == 'yolo\n' * t

