from datetime import datetime

class DatesBr:
    def __init__(self):
        self.moment_register = datetime.today()

    def __str__(self):
            return self.format_data()

    def month_register(self):
        months_year = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]

        month_register = self.moment_register.month - 1
        return months_year[month_register]

    def week_day(self):
        week_day_list = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]

        week_day = self.moment_register.weekday()
        return week_day_list[week_day]
    
    def format_data(self):
        format_data = self.moment_register.strftime("%d/%m/%Y %H:%M")
        return format_data