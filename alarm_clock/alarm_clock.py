class AlarmClock:
    def __init__(self):
        self.current_time = ''
        self.on_off = bool
        self.set_time = ''

    def change_alarm(self):
        self.current_time = input("Please enter current time: ")
        print('The current time is ',self.current_time)

    def alarm_time(self):
        self.set_time = input('Please enter the time you would like your alarm set: ')
        print('The alarm is now set for ',self.set_time)


    def alarm_set(self):
        alarm_status = input('Press 1 to set alarm to on or 2 to set alarm to off. ')
        alarm_on = True
        while alarm_on is True:
            if alarm_status == '1':
                alarm_on = True
                print('The alarm is on.')
            if alarm_status == '2':
                alarm_on = False
                print('The alarm is off.')
            return alarm_status