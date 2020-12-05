def get_pos(seat, index, lower_limit, upper_limit):
    print(seat, index, lower_limit, upper_limit)
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

if __name__ == "__main__":
    seat = "FBFBBFFRLR"
    row, col = get_seat(seat, 128, 8)
    print("Row: ", str(row), ", Col: ", str(col))
