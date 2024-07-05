### 启动worker命令：
```bash
celery -A tasks worker --loglevel=info
```

### 执行python代码发送任务
```bash
python taskpub.py
```

### 注意
* 测试广播任务，需要开启多个终端执行上述命令
* 广播任务，多个worker上收到的任务id是相同的，做result backend会覆盖。

eg：
worker1日志
```vim
[2024-07-05 15:03:12,235: INFO/MainProcess] Task tasks.add[0a22b094-50c9-497c-b052-2faff238490b] received
[2024-07-05 15:03:12,236: INFO/ForkPoolWorker-8] Task tasks.add[0a22b094-50c9-497c-b052-2faff238490b] succeeded in 0.000506999999998925s: 5
[2024-07-05 15:03:12,237: INFO/MainProcess] Task tasks.mul[2070d171-4cd1-4ef7-ac05-c2b9abc9a3ca] received
[2024-07-05 15:03:12,238: INFO/ForkPoolWorker-8] Task tasks.mul[2070d171-4cd1-4ef7-ac05-c2b9abc9a3ca] succeeded in 0.0003297919999880605s: 6
```

worker2日志
```vim
[2024-07-05 15:03:12,237: INFO/MainProcess] Task tasks.mul[2070d171-4cd1-4ef7-ac05-c2b9abc9a3ca] received
[2024-07-05 15:03:12,238: INFO/ForkPoolWorker-8] Task tasks.mul[2070d171-4cd1-4ef7-ac05-c2b9abc9a3ca] succeeded in 0.00029312499999889496s: 6
```
可以看到发送的tasks.mul广播任务，两个worker收到的taskId是一样的
```vim
tasks.mul[2070d171-4cd1-4ef7-ac05-c2b9abc9a3ca]
```
