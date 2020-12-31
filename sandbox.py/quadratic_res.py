from datetime import datetime

def is_quad_res(y, x, zx_set):
    qrs = []

    for w in zx_set:
        if (w ** 2) % x == y % x:
            qrs.append(w)

    return qrs


def gen_set(x):
    zx_set = []

    for y in range(1, x):
        if gcd(x, y) == 1:
            zx_set.append(y)

    return zx_set

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

if __name__ == "__main__":
    x = 887
    zx_set = gen_set(x)

    max_n_of_res = 0

    count = 0
    size = len(zx_set)

    increment = 300

    t_start = datetime.now().timestamp()
    out = ""

    for i in range(size):
        y = zx_set[i]
        qrs = is_quad_res(y, x, zx_set)
        if len(qrs) > 0 :
            #print(y, qrs)
            count += 1
            max_n_of_res = max(max_n_of_res, len(qrs))
            out += "1"
        else:
            out += "0"

        if i % increment == 0 and i != 0:
            t_remaining = int((datetime.now().timestamp() - t_start) * ((size / i) - 1))

            hours = t_remaining // 3600
            minutes = (t_remaining // 60) % 60
            seconds = t_remaining % 60

            timestring = "{hours}h {minutes}m {seconds}s".format(hours = hours, minutes = minutes, seconds = seconds)

            print("ETA:", timestring, "Done:", int((i / size) * 1000) / 10, "%")

    
    print(count / len(zx_set), count, len(zx_set))
    print(max_n_of_res)
    print(out)
