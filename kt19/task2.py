#использование агента для асинхронного обновления состояния

import concurrent.futures
import time

class Agent:
    def __init__(self, initial_value):
        self._value = initial_value

    def send(self, update_func):
        self._value = update_func(self._value)

    def get(self):
        return self._value

agent = Agent(0)

def update_agent(agent, value):
    time.sleep(1)
    agent.send(lambda x: x + value)

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(update_agent, agent, i) for i in range(1, 4)]

concurrent.futures.wait(futures)
print(agent.get())