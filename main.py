from sensor.logger import logging
from sensor.exception import SensorException
import sys,os





if __name__== "__main__":
    try:
        test_logger_and_exception()
        
    except Exception as e:
        print(e)
        