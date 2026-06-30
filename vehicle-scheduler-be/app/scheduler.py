def schedule_tasks(vehicles, max_hours):
    n = len(vehicles)

    dp = [[0]*(max_hours+1) for _ in range(n+1)]

    for i in range(1, n+1):
        duration = vehicles[i-1]["Duration"]
        impact = vehicles[i-1]["Impact"]

        for h in range(max_hours+1):

            if duration <= h:
                dp[i][h] = max(
                    impact + dp[i-1][h-duration],
                    dp[i-1][h]
                )
            else:
                dp[i][h] = dp[i-1][h]

    selected = []

    h = max_hours

    for i in range(n, 0, -1):

        if dp[i][h] != dp[i-1][h]:

            selected.append(vehicles[i-1])

            h -= vehicles[i-1]["Duration"]

    selected.reverse()

    hours = sum(x["Duration"] for x in selected)
    impact = sum(x["Impact"] for x in selected)

    return selected, hours, impact