from tasks import add
from tasks import mul


def pub():
    print("add(1, 2): " + str(add(1, 2)))
    result = add.delay(2, 3)
    print("result = app.AsyncResult(id) result:" + str(result))
    if result.ready():
        get = result.get()
        print("result.get() get:" + str(get))
    else:
        print("result not ready")
    get = result.get(timeout=1)
    print("result.get(timeout=1) get:" + str(get))
    mul_delay = mul.apply_async(args=[2, 3], broadcast=True, queue='broadcast_tasks')
    print(str(mul_delay.get(timeout=1)))


if __name__ == '__main__':
    pub()
