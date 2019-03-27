import Simulator;

def main():
    sim = Simulator.Simulator();
    for i in range(1,6) :
        sim.loadMemory ("input/input"+str(i));
        sim.simulate ();
        sim.storeMemory ("output/output"+str(i));

    '''for i in range(1,6) :
        sim.loadMemory2 ("input/input"+str(i));
        sim.simulate2 ();
        sim.storeMemory ("output/output"+str(i));'''

if __name__ == '__main__':
	main();
