#BPM to ms/Hz Calculator
import os

print("\n")
title = 'BPM to ms/hz Calculator v1.0'.center(os.get_terminal_size().columns)
print('\n', title)

# Switch to enable user to quit
on = True

while on:
    # Prompt User input
    print('Enter Tempo (BPM) or \'q\' to quit:')
    bpm = input()

    if bpm == 'q':
        on = False
    # begin loop again if User didn't enter a number
    elif bpm.isdigit() == False:
        pass
    else:
        # derives quarter-note ms value for tempo
        # 600000 milliseconds (in a minute) / tempo (beats-per-minute)
        qv = 60000 / int(bpm) 

        #store calculations for beat sub-divisions [quarter-note is the base unit]
        # e.g. at 120 bpm, every 1/8th note is 250 ms apart
        # * = dotted; T = triplet
        divisions = {           
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
        
        print('\n')
        # table header
        col1 = 'Division'
        col2 = 'Delay Time (ms)'
        print(f'{col1} | {col2} @ Tempo = {bpm}')
        # table formatting
        table_frame = ' '.join(['-' * len(col1), '+', '-' * len(col2)])
        print(table_frame) 

        # display calculations
        for div, time in divisions.items():
            delay = format(time, '.2f')
            # .ljust pads the 1st column so that the table_frame lines up
            print(f'{div.ljust(8)} | {delay}') 
            print(table_frame)
        print('\n')
        
