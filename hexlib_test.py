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
# get the checksum of a given record
hx = ':20A04000000000000000000000000000000000000000000000000000000000000000000000'
print(hexlib.record_checksum_control(hx))

# get_checksum()
print(hexlib.get_checksum(hx))
