import hexlib

testrec = ':202A8000000080264B65305091900028D922A0D291900008D90092E2233688E34B5E305047'

# le2be()
# code here

# read_record()
print(hexlib.read_record(testrec))

# data2int()
# code here

# data2float()
# code here

# checksum_control()
hx = ':0300300002337A1E'
print(hexlib.checksum_control(hx))

# get_checksum()
print(hexlib.get_checksum(testrec))