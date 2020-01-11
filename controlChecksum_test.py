import controlChecksum

result = controlChecksum.controlChecksum('A193846_TCU_SW_8RC0125_HBQBL_CzKzzz_HILParams181130.hex')

if True == result:
    print('check passed.')
else:
    print('check failed.')