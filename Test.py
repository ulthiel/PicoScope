import sys
sys.path.insert(0, "lib/picosdk-python-examples/python-picoscope/picoscope/")
import ps2000a
ps = ps2000a.Device()	

status = ps.open_unit()
print ps.info
ps.close_unit()