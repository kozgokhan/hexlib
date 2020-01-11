
# convert little endian to big endian
def le2be(lestr):
    be = ''
    for i in range(0, len(lestr), 2):
        be = lestr[i:i+2] + be
    return be

# read a record line and return a list
def read_record(recordstr):
    if ':' != recordstr[0]:
        return 0
    else:
        byte_count = int(recordstr[1:3], 16)
        address = recordstr[3:7]
        record_type = recordstr[7:9]
        data = recordstr[9:(len(recordstr)-2)]
        checksum = recordstr[(len(recordstr)-2):]

        return [byte_count, address, record_type, data, checksum]

# convert hex data to integer
def data2int(datastr, sign, bytenum, resolution, minval, maxval, offset):
    if (0 != sign):
        return max(min(offset + resolution * int(datastr, 16) - 2**(bytenum*8), maxval), minval)
    else:
        return max(min(offset + resolution * int(datastr, 16), maxval), minval)

# check if the checksum correct
def checksum_control(record):
    reclen = len(record)
    sum = 0
    for i in range(1, reclen-2, 2):
        sum += int('0x' + record[i:i+2], 16)
    
    sumhex = hex(sum)
    comp = 256 - int(sumhex[len(sumhex)-2:], 16)

    return comp == int('0x' + record[(reclen-2):], 16)


# get the checksum of a given record
def get_checksum(record):
    reclen = len(record)
    sum = 0
    for i in range(1, reclen-2, 2):
        sum += int('0x' + record[i:i+2], 16)
    
    sumhex = hex(sum)
    return hex(256 - int(sumhex[len(sumhex)-2:], 16))