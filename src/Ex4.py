import json
from src.TheGame import TheGame
from src.client import Client
from src.GUI import gui

PORT = 6666
HOST = '127.0.0.1'
client = Client()
client.start_connection(HOST, PORT)

main = TheGame()


def getAllAgents():
    numberOfAgents = int(json.loads(client.get_info())["GameServer"]["agents"])
    for i in range(numberOfAgents):
        client.add_agent("{\"id\":" + str(i) + "}")


getAllAgents()
main.setNewVal(client.get_agents(), client.get_graph(), client.get_pokemons())
gui = gui(main, client)
client.start()
while client.is_running():
    main.setNewVal(client.get_agents(), client.get_graph(), client.get_pokemons())
    for agent in main.AgentsList.values():
        main.allocateAgent(agent)
    for agent in main.AgentsList.values():
        if agent.dest == -1 and agent.Next is not None:
            client.choose_next_edge(
                '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(agent.Next) + '}')
            agent.Next = None
    gui.drawAll()
    main.sleep()
    client.move()
