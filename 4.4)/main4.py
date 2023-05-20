

def is_lucky_ticket(ticket_num):
    if len(ticket_num) % 2 != 0:
        return False
    half_len = len(ticket_num) // 2
    first_half = ticket_num[:half_len]
    second_half = ticket_num[half_len:]
    sum_first = sum(map(int, first_half))
    sum_second = sum(map(int, second_half))
    if sum_first == sum_second:
        return True
    else:
        return False
print(is_lucky_ticket("385916"))
