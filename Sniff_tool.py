for i in range(0,len(results_ans)):
        # psrc stands for source IP Address
        # hwsrc stands for destination MAC Address
        clients_data = {"ip":results_ans[i][0].psrc," mac":results_ans[i][1].hwsrc}
        results.append(clients_data)
        clients = {"ip":results_ans[i][1].psrc," mac":results_ans[i][1].hwsrc}
        results.append(clients)
    for i in range(len(results)):
        print(results[i])
