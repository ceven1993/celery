from kombu.common import Broadcast, Queue, Exchange

from celery import Celery

app = Celery('tasks', broker='redis://localhost', backend='redis://localhost')
# redis作broker时广播任务配置方式只有下面这种好使，不要乱改
q = Queue('broadcast_tasks', Exchange('broadcast_tasks', type='fanout'), )
app.conf.task_queues = (q, Queue('celery'), )
app.conf.task_routes = {
    'tasks.mul': {
        'queue': 'broadcast_tasks',
    }
}


@app.task()
def add(x, y):
    return x + y


@app.task()
def mul(x, y):
    return x * y


if __name__ == '__main__':
    app.start()
