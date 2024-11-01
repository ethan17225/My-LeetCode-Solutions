class Solution:
    def reformatDate(self, date: str) -> str:
        MONTH_TO_NUMBER = {
            "Jan": "01", "Feb": "02", "Mar": "03",
            "Apr": "04", "May": "05", "Jun": "06",
            "Jul": "07", "Aug": "08", "Sep": "09",
            "Oct": "10", "Nov": "11", "Dec": "12"
        }

        formated_date = []
        date_component = date.split()

        formated_date.append(date_component[-1])
        formated_date.append(MONTH_TO_NUMBER.get(date_component[-2], " "))
        day = []
        for c in date_component[-3]: 
            if c.isdigit():
                day.append(c)
            else:
                break

        if len(day) == 1:
            day.insert(0, "0")

        formated_date.append("".join(day))


        return "-".join(formated_date)



