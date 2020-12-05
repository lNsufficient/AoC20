def get_pos(seat, index, lower_limit, upper_limit):
    if lower_limit == upper_limit:
        return index, lower_limit

    #always split range in two equal parts:
    new_limit = (upper_limit + lower_limit + 1)/2
    if seat[index] in "BR":
        lower_limit = new_limit
    elif seat[index] in "FL":
        upper_limit = new_limit - 1 #zero indexing - reduce by 1
    
    return get_pos(seat, index + 1, lower_limit, upper_limit)

def get_seat(seat, nbr_rows, nbr_cols):
    # zero indexing: upper limit is nbr_rows - 1
    index, row = get_pos(seat, 0, 0, nbr_rows - 1)

    # zero indexing: upper limit is nbr_cols - 1  
    index, col = get_pos(seat, index, 0, nbr_cols - 1)
    
    return int(row), int(col)

def get_seat_id(row, col):
    return row*8 + col

def get_seat_info(seat):
    row, col = get_seat(seat, 128, 8)
    seat_id = get_seat_id(row, col) 
    return row, col, seat_id

def print_seat_info(seat, row, col, seat_id):
    print("Seat: " + str(seat))
    print("Row: " + str(row) + ", Col: " + str(col))
    print("Seat ID: " + str(seat_id) + "\n")


if __name__ == "__main__":
    seats = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    for seat in seats:
        seat_info = get_seat_info(seat)
        print_seat_info(seat, *seat_info)

    print("Highest seat ID: " + str(get_seat_id(127, 7)))