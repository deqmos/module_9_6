def all_variants(text):
    start = 0
    end = 1
    len_str = 1
    while len_str <= len(text):
        yield text[start:end]
        start += 1
        end += 1
        if end > len(text):
            start = 0
            len_str += 1
            end = len_str


a = all_variants("abc")
for i in a:
    print(i)
