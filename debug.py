import datetime


class Debug:
    @staticmethod
    def GetTime() -> str:
        now: datetime.datetime = datetime.datetime.now()
        return f"{now.year} {now.month} {now.day}/{now.hour}:{now.minute}:{now.second} - "

    @staticmethod
    def Log(msg: str) -> None:
        print(Debug.GetTime() + msg)
