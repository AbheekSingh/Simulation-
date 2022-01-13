from ExploitOnly import *
from ExploreOnly import *
from eGreedy import *

def Simulate_Explore(t: int):
    happiness_avg = 11
    days = 300
    totalhappiness, totalregret = 0, 0
    print("\nExplore only:")
    optimum = happiness_avg * days
    expectedtotal = 100*9 + 100*7 + 100*11
    regret = optimum - expectedtotal
    print("Optimum Happiness: " + str(optimum) + " Expected Total Happiness: " + str(expectedtotal) + " Expected Regret: " + str(regret))
    for i in range(t):
        exploreVar = exploreOnly()
        totalhappiness = totalhappiness + exploreVar
        regret = optimum - exploreVar
        totalregret = totalregret + regret
    avgTotalHappiness = totalhappiness / t
    avgRegret = totalregret / t
    print("Average Total Happiness: " + str(avgTotalHappiness) + " Average Regret: " + str(avgRegret))


def Simulate_eGreedy(t: int, e: int):
    happiness_avg = 11
    days = 300
    totalhappiness, totalregret = 0, 0
    print("\neGreedy:")
    optimum = happiness_avg * days
    eGreedy_dec = e/100
    expectedtotal = (1 - eGreedy_dec) * 300 * 11 + (eGreedy_dec / 3) * 300 * 9 + (eGreedy_dec / 3) * 300 * 7 + (eGreedy_dec / 3) * 300 * 11
    regret = optimum - expectedtotal
    print("Optimum Happiness: " + str(optimum) + " Expected Total Happiness: " + str(expectedtotal) + " Expected Regret: " + str(regret))
    for i in range(300):
        greedyVar = e_greedy(e)
        totalhappiness = totalhappiness + greedyVar
        regret = optimum - greedyVar
        totalregret = totalregret + regret
    avgTotalHappiness = totalhappiness / t
    avgRegret = totalregret / t
    print("Average Total Happiness: " + str(avgTotalHappiness) + " Average Regret: " + str(avgRegret))


def Simulate_Exploit(t: int):
    happiness_avg = 11
    days = 300
    totalhappiness, totalregret = 0, 0
    print("\nExploit only:")
    print("This is the data after " + str(t) + " trails...\n")
    optimum = happiness_avg * days
    expectedtotal = 9 + 7 + 11 + 297*11
    regret = optimum - expectedtotal
    print("Optimum Happiness: " + str(optimum) + " Expected Total Happiness: " + str(expectedtotal) + " Expected Regret: " + str(regret))
    for i in range(t):
        exploitVar = exploitOnly()
        totalhappiness = totalhappiness + exploitVar
        regret = optimum - exploitVar
        totalregret = totalregret + regret
    avgTotalHappiness = totalhappiness / t
    avgRegret = totalregret / t
    print("Average Total Happiness: " + str(avgTotalHappiness) + " Average Regret: " + str(avgRegret))

def Simulation(times: int, eGre: int):
    Simulate_Exploit(times)
    Simulate_Explore(times)
    Simulate_eGreedy(times, eGre)


Simulation(100, 1)
Simulation(10000, 20)
Simulation(100000, 20)