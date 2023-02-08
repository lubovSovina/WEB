import datetime
import schedule

i = 1


def job():
    global i
    print(f"Запустился {i} раз")
    i += 1
    print(datetime.datetime.now())


schedule.every(5).seconds.do(job)
# schedule.every(10).minutes.do(job)  # каждые 10 минут
# schedule.every().hour.do(job)  # каждый час
# schedule.every().day.at("10:30").do(job)  # каждый день в 10-30
# schedule.every().monday.do(job)  # каждый понедельник
# schedule.every(2).wednesday.at("13:15").do(job)  # Каждую вторую среду в 13-15
# schedule.every().minute.at(":17").do(job)  # каждую минуту в 17 секунду

while True:
    schedule.run_pending()
