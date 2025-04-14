import serial
import time
import sqlite3
import datetime
import telepot 
bot=telepot.Bot("7627300344:AAFIyy5mIo0YD25Btzf5h5URJcRXO9Zzldk")
ch_id="7716182006"
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS sensors(time TEXT, enginetemp TEXT, voltage TEXT, current TEXT, temp TEXT, smoke TEXT, vibration TEXT, oillevel TEXT)"""
cursor.execute(command)

data = serial.Serial(
                  'COM3',
                  baudrate = 9600,
                  parity=serial.PARITY_NONE,
                  stopbits=serial.STOPBITS_ONE,
                  bytesize=serial.EIGHTBITS,                  
                  timeout=1
                  )
def Send(a):
  data.write(str.encode(a))
  print(f'sent............{a}')



def Read_Data():
    d = data.readline()
    d = d.decode('UTF-8', 'ignore')
    d = d.strip()
    print(d)
    if d:
        d = d.split(',')
        # print(f"start\n\n\n{d}\n\nend")
        if len(d) == 7:
            if float(d[0]) > 30:  ## Engine_Temp
                d0="High"
                Send("A")
                bot.sendMessage(ch_id,"Engine Temperature is got high")
            else:  ## Engine_Temp
                d0="Normal"

            if float(d[1]) > 10:  ## Voltage
                d1="High"
                Send("A")
                bot.sendMessage(ch_id,"Voltage is got high")
            else:  ## Voltage
                d1="Normal"

            if float(d[2]) > 4:  ## current
                d2="High"
                Send("A")
                bot.sendMessage(ch_id,"Current flow  is high")
            else:  ## current
                d2="Normal"


            if float(d[3]) > 30:  ## battery temp
                d3="High"
                Send("A")
                bot.sendMessage(ch_id,"Engine Temperature is got high")
            else:  ## battery temp
                d3="Normal"


            if float(d[4]) > 700:  ## smoke
                d4="Heavy Smoke"
                Send("A")
                bot.sendMessage(ch_id,"Smoke Detected")
            else:  ## smoke
                d4="No Smoke"

            if float(d[5]) == 0 :  ## vibration
                d5="No vibration"
            else:  ## vibration
                d5="Vibration"
                Send("A")
                bot.sendMessage(ch_id,"Sensed Vibration !! \n ")


            if float(d[6]) > 15:  ## oil_level
                d6="Oil low "
                Send("A")
                bot.sendMessage(ch_id,"Oil level is low ")
            else:  ## oil_level
                d6="sufficient oil"

            # status=f" Predictive maintance of Automobiles \n\n Status : \n\n Engine Temperature : {d0} \nVoltage : {d1} \nCurrent : {d2} \nBattery Temp : {d3} \nSmoke Level : {d4} \nVibration : {d5} \nOil level : {d6} "
            # bot.sendMessage(ch_id,status)

            from datetime import datetime
            current_time = datetime.now()
            Date = current_time.strftime("%H:%M:%S")
            
            cursor.execute('insert into sensors values(?,?,?,?,?,?,?,?)',[Date, d[0], d[1], d[2], d[3], d[4],d[5], d[6]] )
            connection.commit()

    time.sleep(0.5)
