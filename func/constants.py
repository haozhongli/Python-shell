__author__ = 'lenovo'
import os

SHELL_STATUS_STOP = 0
SHELL_STATUS_RUN = 1

# ʹ�� os.path.expanduser('~') ��ȡ��ǰ����ϵͳƽ̨�ĵ�ǰ�û���Ŀ¼
HISTORY_PATH = os.path.expanduser('~') + os.sep + '.Ubuntu_shell_history'
