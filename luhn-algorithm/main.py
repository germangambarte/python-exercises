card1 = "5371263336363050"
card4 = "7992739871"
card2 = str(5270084271610509)
card3 = str(5536143272189040)


def validate_cc(cc):
    cache = dict()
    sum = 0
    count_cache = 0;
    count_not_cache = 0;
    for i in range(len(cc) - 1, -1, -1):
        if i % 2 != 0:
            if cache.keys().__contains__(cc[i]):
                sum += cache[cc[i]]
                count_cache += 1
                continue
            count_not_cache += 1
            value = int(cc[i]) * 2
            if value > 9:
                value = value - 9
            sum += value
            cache[cc[i]] = value
        else:
            sum += int(cc[i])
    print(f"cache: {count_cache}")
    print(f"not cache: {count_not_cache}")
    return 10 - (sum % 10)


validation_digit = validate_cc(card1)
is_valid = validate_cc(card1 + str(validation_digit)) == 0
print(f"{validation_digit} {card1 + str(validation_digit)}")
print(is_valid)
