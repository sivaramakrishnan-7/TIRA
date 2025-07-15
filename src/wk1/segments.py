def find_segments(data):
    out = []
    i = 0
    while i < len(data):
        curr_data = data[i]
        count = 1
        while i+1 < len(data) and data[i+1] == curr_data:
            count += 1
            i+=1
        out.append((count, curr_data))
        i+=1
    return out



if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]
