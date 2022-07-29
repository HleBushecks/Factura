import csv


def finish(factura, names):
    results = []

    def result_func(same, data):
        hour = 0
        result = []
        for name in same:
            hour += factura[name][data][1]
        result.append(f'{data + 1}.7.2022')
        result.append(factura[same[0]][data][0])
        result.append(hour)
        for name in same:
            result.append(f'{name}/{factura[name][data][1]} hod')
        results.append(result)

    for data in range(0, 31):
        same = []
        for name1 in names:
            if name1 in same or factura[name1][data][1] == 0:
                continue
            same = []
            for name2 in names:
                if factura[name1][data][0] == factura[name2][data][0]:
                    if factura[name2][data][1] == 0:
                        continue
                    same.append(name2)
            result_func(same, data)

    with open("book.csv", 'r') as file:
        res = csv.reader(file)
        old_result = []
        q = ''
        for i in res:
            old_result.append(i)
            q = q + str(i)

    new_result = []
    if old_result == []:
        with open('book.csv', 'w') as file:
            writer = csv.writer(file)
            for i in results:
                writer.writerow(i)
    else:
        for i in old_result:
            for ii in results:
                lidi = ii[3:]
                if i[0] == ii[0] and i[1] == ii[1]:
                    for iii in lidi:
                        if iii not in i:
                            i[2] = float(i[2]) + float(iii.split('/')[1].split(' ')[0])
                            i.append(iii)
                elif i[0] == ii[0] and i[1] != ii[1] and f"'{ii[0]}', '{ii[1]}'" not in q:
                    new_result.append(ii)
                    q = q + str(ii)
                elif ii[0] not in q:
                    q = q + str(ii)
                    new_result.append(ii)
            new_result.append(i)
        with open('book.csv', 'w') as file:
            writer = csv.writer(file)
            for i in new_result:
                writer.writerow(i)

    with open('book.csv', 'r') as file:
        f = csv.reader(file)
        res = []
        for i in list(f):
            if '.0' in i[2]:
                i[2] = i[2][:-2]
                res.append(i)
            else:
                res.append(i)
        res = sorted(res, key=lambda x: int(x[0].split('.')[0]))
    with open('book.csv', 'w') as file:
        writer = csv.writer(file)
        for i in res:
            writer.writerow(i)


if __name__ == "__main__":
    pass
