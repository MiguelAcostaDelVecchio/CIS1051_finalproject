import numpy as np

def initial_price(stock, data):
    np_data = data[stock]["Close"].to_numpy()
    So = np_data[-1]
    return So

# [----------------- Evaluate needed parameters for Monte Carlo Simulation ------------]
def analysis(stock, data, num_simulations):
    # Parameter Definitions

    # So    :   initial stock price
    # dt    :   time increment -> a day in our case
    # T     :   length of the prediction time horizon(how many time points to predict, same unit with dt(days))
    # N     :   number of time points in the prediction time horizon -> T/dt
    # t     :   array for time points in the prediction time horizon [1, 2, 3, .. , N]
    # mu    :   mean of historical daily returns
    # sigma :   standard deviation of historical daily returns
    # b     :   array for brownian increments
    # W     :   array for brownian path

    # Formula -> dS = So * ((mu * dt) + (sigma * random_num * sqrt(dt)))

    # Evaluate So
    np_data = data[stock]["Close"].to_numpy()
    So = np_data[-1]
    # print(So)

    # Evaluate dt
    dt = 1

    # Evaluate T
    T = len(np_data)
    # print(T)

    # Evaluate N
    N = T / dt
    # print(N)

    # Evaluate t
    t = np.arange(1, int(N) + 1)
    # print(t)

    # Evaluate mu
    returns = []
    for ele in range(0, len(t)):
        if ele == 0:
            returns.append((np_data[ele] - np_data[ele - 1]) / (np_data[-1] * 100))
        else:
            returns.append((np_data[ele] - np_data[ele - 1]) / np_data[-1])
    # print(returns)
    mu = np.mean(returns)
    # print(mu)

    # Evaluate Sigma
    sigma = np.std(returns)
    # print(sigma)

    # Evaluate b
    b = {str(num): np.random.normal(0, 1, int(N)) for num in range(1, num_simulations + 1)}
    # print(b)

    # Evaluate W
    W = {str(num): b[str(num)].cumsum() for num in range(1, num_simulations + 1)}
    # print(W)

    # Evaluating drift and diffusion
    drift = (mu - 0.5 * sigma ** 2) * t
    # print("drift:\n", drift)
    diffusion = {str(num): sigma * W[str(num)] for num in range(1, num_simulations + 1)}
    # print("diffusion:\n", diffusion)

    S = np.array([So * np.exp(drift + diffusion[str(num)]) for num in range(1, num_simulations + 1)])
    S = np.hstack((np.array([[So] for num in range(num_simulations)]), S))
    # print(S)
    return S, So, stock
# [------------------------- End of Analysis -------------------------]


# What is the probability of the stock price going up by at least 20% after 1 year?
def stock_prob(S, So, ticker, threshold, num_simulations):
    cnt = 0
    for i in range(num_simulations):
        if threshold >= 1:
            if (S[i, -1] / So) > threshold:
                cnt += 1
        else:
            if (S[i, -1] / So) < threshold:
                cnt += 1
    prob = cnt / num_simulations
    print("\nPrice of {} at which simulation begins is ${}".format(ticker, So))
    print("The probability that the stock price will go up/down by {}% in one year is {}%\n".format(
        round((threshold - 1) * 100, 2), prob * 100))

    return prob


def buy_stock(stock_name, prob, confidence):
    if prob >= confidence:
        return stock_name, "Buy"
    else:
        return stock_name, "Next stock"