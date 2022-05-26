import psutil
import logging

print('The CPU usage is: ', psutil.cpu_percent(4))
print(psutil.virtual_memory())
logging.basicConfig(filename="test.txt", level=logging.DEBUG)
logging.debug(psutil.cpu_percent(4))
logging.debug(psutil.virtual_memory())
