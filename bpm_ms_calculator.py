#BPM to ms/Hz Calculator
import os

print("\n")
print('BPM to ms/hz Calculator v1.0'.center(os.get_terminal_size().columns))

on = True
while on:
    print('Enter Tempo (BPM) or \'q\' to quit:')
    bpm = input()
    if bpm == 'q':
        on = False
        break
    elif bpm.isdigit() == False:
        pass
    else:
        qv = 60000 / int(bpm) # derives quarter-note ms value for tempo

        divisions = {           #dictionary to store calculations for beat sub-divisions using quartner-note as basic unit
            '1/2*': qv*3,
            '1/2': qv*2,
            '1/2T':qv/3*4,
            '1/4*': qv*1.5,
            '1/4': qv,
            '1/4T':qv/3*2,
            '1/8*': qv/2*1.5,
            '1/8': qv/2,
            '1/8T':qv/3,
            '1/16*': qv/4*1.5,
            '1/16': qv/4,
            '1/16T':qv/6,
            '1/32*': qv/8*1.5,
            '1/32': qv/8,
            '1/32T':qv/12,
            '1/64*': qv/16*1.5,
            '1/64': qv/16,
            '1/64T':qv/24,
            '1/128*': qv/32*1.5,
            '1/128': qv/32,
            '1/128T':qv/48,
            }
        print("\n")  #separates table values from input line
        print("{0} | {1} | {2}".format('Division', 'Delay Time (ms)', 'Tempo = ' + bpm)) #prints table header
        for k, v in divisions.items():
            print("{0} | {1}".format(k.ljust(7), format(v, '.2f'))) #prints sub-divisions into table format
        print("\n")
