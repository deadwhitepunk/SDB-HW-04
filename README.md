# Домашнее задание к занятию  «Очереди RabbitMQ»

### Желонкин Дмитрий

### Задание 1. Установка RabbitMQ

Используя Vagrant или VirtualBox, создайте виртуальную машину и установите RabbitMQ.
Добавьте management plug-in и зайдите в веб-интерфейс.

*Итогом выполнения домашнего задания будет приложенный скриншот веб-интерфейса RabbitMQ.*

![Админка RabbitMQ](https://github.com/deadwhitepunk/sdb-hw-04/blob/main/img/image_admin_rabbitmq.png)

---

### Задание 2. Отправка и получение сообщений

Используя приложенные скрипты, проведите тестовую отправку и получение сообщения.
Для отправки сообщений необходимо запустить скрипт producer.py.

Для работы скриптов вам необходимо установить Python версии 3 и библиотеку Pika.
Также в скриптах нужно указать IP-адрес машины, на которой запущен RabbitMQ, заменив localhost на нужный IP.

```shell script
$ pip install pika
```

Зайдите в веб-интерфейс, найдите очередь под названием hello и сделайте скриншот.
После чего запустите второй скрипт consumer.py и сделайте скриншот результата выполнения скрипта

*В качестве решения домашнего задания приложите оба скриншота, сделанных на этапе выполнения.*

![Отправка сообщений](https://github.com/deadwhitepunk/sdb-hw-04/blob/main/img/image_send_messages.png)

Выполнение скрипта consumer.py

![Получение сообщений](https://github.com/deadwhitepunk/sdb-hw-04/blob/main/img/image_unpacked_messages.png)

Очередь после принятия сообщений:

![Получение сообщений очередь в админке](https://github.com/deadwhitepunk/sdb-hw-04/blob/main/img/image_unp_mess_adm.png)

---

### Задание 3. Подготовка HA кластера

Используя Vagrant или VirtualBox, создайте вторую виртуальную машину и установите RabbitMQ.
Добавьте в файл hosts название и IP-адрес каждой машины, чтобы машины могли видеть друг друга по имени.

Пример содержимого hosts файла:
```shell script
$ cat /etc/hosts
192.168.0.10 rmq01
192.168.0.11 rmq02
```
После этого ваши машины могут пинговаться по имени.

Затем объедините две машины в кластер и создайте политику ha-all на все очереди.

*В качестве решения домашнего задания приложите скриншоты из веб-интерфейса с информацией о доступных нодах в кластере и включённой политикой.*

![Кластер в админке](https://github.com/deadwhitepunk/sdb-hw-04/blob/main/img/image_cluster1.png)

![Политика HA](https://github.com/deadwhitepunk/sdb-hw-04/blob/main/img/image_cluster_policies.png)

Также приложите вывод команды с двух нод:

```shell script
$ rabbitmqctl cluster_status
```

![Статус кластера на нодах](https://github.com/deadwhitepunk/sdb-hw-04/blob/main/img/image_status_cluster.png)

Для закрепления материала снова запустите скрипт producer.py и приложите скриншот выполнения команды на каждой из нод:

```shell script
$ rabbitmqadmin get queue='hello'
```

![Очередь hello](https://github.com/deadwhitepunk/sdb-hw-04/blob/main/img/image_console_get_queue.png)

После чего попробуйте отключить одну из нод, желательно ту, к которой подключались из скрипта, затем поправьте параметры подключения в скрипте consumer.py на вторую ноду и запустите его.

*Приложите скриншот результата работы второго скрипта.*

![Консюмер после отключения ноды](https://github.com/deadwhitepunk/sdb-hw-04/blob/main/img/image_turnoff_node.png)

## Дополнительные задания (со звёздочкой*)
Эти задания дополнительные, то есть не обязательные к выполнению, и никак не повлияют на получение вами зачёта по этому домашнему заданию. Вы можете их выполнить, если хотите глубже шире разобраться в материале.

### * Задание 4. Ansible playbook

Напишите плейбук, который будет производить установку RabbitMQ на любое количество нод и объединять их в кластер.
При этом будет автоматически создавать политику ha-all.

[Vagrant file](https://github.com/deadwhitepunk/sdb-hw-04/blob/main/RabbitMQ/Ansible/Vagrantfile)
[Ansible playbook](https://github.com/deadwhitepunk/sdb-hw-04/blob/main/RabbitMQ/Ansible/playbook.yml)