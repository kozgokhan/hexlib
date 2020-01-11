import hexlib

def controlChecksum(filename):
    status = True

    file = open(filename, 'r')
    lines = file.readlines()

    for line in lines:
        if (line.endswith('\n')):
            line = line[0:-1]
        if (':' == line[0] and False == hexlib.record_checksum_control(line)):
            status = False
            print(line)
    
    return status