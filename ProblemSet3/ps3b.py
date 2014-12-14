# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamic

import random
import numpy
import pylab

'''
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.max_birth_prob = maxBirthProb
        self.clear_prob = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.max_birth_prob

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clear_prob

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """

        return random.random() <= self.getClearProb()


    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        if random.random() < self.getMaxBirthProb() * (1-popDensity):
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        else:
            raise NoChildException()

class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.max_pop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.max_pop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population.
        returns: The total virus population (an integer)
        """

        return len(self.viruses)


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update()

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.

        returns: The total virus population at the end of the update (an
        integer)
        """

        # create copy of self.viruses to iterate over
        self.viruses_temp = []

        # iterate over self.viruses_copy to check if virus survives or not
        for virus in self.viruses:
            if not virus.doesClear():
                self.viruses_temp.append(virus)

        self.viruses = self.viruses_temp[:]

        # calculate current population density
        self.pop_density = float(len(self.viruses)) / self.getMaxPop()

        # create another copy of self.viruses to iterate over
        self.viruses_copy = self.viruses[:]

        # append to current self.virus list the viruses that reproduce
        for self.virus in self.viruses_copy:
            try:
                self.viruses.append(self.virus.reproduce(self.pop_density))
            except NoChildException:
                pass

        # return virus population
        return len(self.viruses)

# test cases
#
# virus = SimpleVirus(1.0, 1.0)
# patient = Patient([virus], 100)
# patient.update()
#
# viruses = [ SimpleVirus(0.56, 0.81), SimpleVirus(0.85, 0.72) ]
# P1 = Patient(viruses, 8)
# P1.getTotalPop()
# P1.update()

#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    # initialize time_steps (300)
    time_steps = 300

    # initialize results as list
    results = []

    # initialize results with number of lists = time_steps
    for i in range(time_steps):
        results.append([])

    # for each trial in numTrial:
    for trial in range(numTrials):

        # initialize virus_list with maxBirthProb and clearProb
        virus_list = []

        for virus in range(numViruses):
            virus_list.append(SimpleVirus(maxBirthProb, clearProb))

        # initialize patient with maxPop
        patient = Patient(virus_list, maxPop)

        # for each time_step in time_steps
        for time_step in range(time_steps):

            # append to result[time_step] the update from each time_step
            results[time_step].append(patient.update())

    # calculate average of each time_step across trials by dividing each time_step list by numTrials
    result_average = []

    for time_step in results:
        result_average.append(sum(time_step) / float(numTrials))

    # plot graph
    pylab.plot(result_average, label = 'Total Virus Population')
    pylab.title('SimpleVirus simulation')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Virus Population')
    pylab.legend(loc = 'best')
    pylab.show()

# simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)

#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self,maxBirthProb,clearProb)
        self.max_birth_prob = maxBirthProb
        self.clear_prob = clearProb
        self.resistances = dict(resistances)
        self.mut_prob = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return dict(self.resistance)

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mut_prob

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return self.resistances.get(drug, False)

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        # initialize resist_check to be true
        resist_check = True

        # if the virus is not resistance to any drug in activeDrugs,
        # change resist check to False and break
        for drug in activeDrugs:
            if not self.isResistantTo(drug):
                resist_check = False
            break

        # if the drug is resistance to all drugs
        if resist_check:

            # initialize copy of resistances
            resistance_list = self.resistances.copy()

            # check if virus reproduces
            if random.random() < self.max_birth_prob * (1 - popDensity):

                # if drug reproduces, for each drug in resistance list, check for mutation
                for drug_res in resistance_list:

                    if resistance_list[drug_res]:
                        if random.random() > 1 - self.mut_prob:
                            resistance_list[drug_res] = False

                    else:
                        if random.random() > 1 - self.mut_prob:
                            resistance_list[drug_res] = True

                return ResistantVirus(self.max_birth_prob, self.clear_prob, resistance_list, self.mut_prob)
            raise NoChildException()

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self, viruses, maxPop)
        self.viruses = viruses
        self.maxPop = maxPop
        self.postcondition = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.postcondition:
            self.postcondition.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.postcondition

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # initialize population of resistant viruses = 0
        resist_pop = 0

        for virus in self.viruses:
            resist = True

            for drug in drugResist:

                if not virus.isResistantTo(drug):
                    resist = False
                    break

            if resist:
                resist_pop += 1

        return resist_pop

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        # create copy of self.viruses to iterate over
        self.viruses_temp = []

        # iterate over self.viruses to check if virus survives or not
        for virus in self.viruses:
            if not virus.doesClear():
                self.viruses_temp.append(virus)

        self.viruses = self.viruses_temp[:]

        # calculate current population density
        self.pop_density = float(len(self.viruses)) / self.getMaxPop()

        # create another copy of self.viruses to iterate over
        self.viruses_copy = self.viruses[:]
        self.new_viruses = []

        # append to current self.virus list the viruses that reproduce
        for self.virus in self.viruses_copy:
            try:
                self.new_viruses.append(self.virus.reproduce(self.pop_density, self.postcondition))
            except NoChildException:
                pass

        self.viruses += self.new_viruses

        # return virus population
        return len(self.viruses)

virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
virus2 = ResistantVirus(1.0, 0.0, {"drug1": False}, 0.0)
patient = TreatedPatient([virus1, virus2], 1000000)
patient.addPrescription("drug1")
patient.update()

#
# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    def runTrialDrug(elapsedTimeSteps, numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, tempResistPopList):
        viruses = [];
        for i in range(numViruses):
            virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb);
            viruses.append(virus);

        patient = TreatedPatient(viruses, maxPop);

        virusLevelsThisTrial = [];
        ResistPopListThisTrial = [];
        ResistPopListThisTrial.append(patient.getResistPop(patient.getPrescriptions()));
        virusLevelsThisTrial.append(patient.getTotalPop());

        for i in range(elapsedTimeSteps):
            if i == 150:
                patient.addPrescription('guttagonol');

            virusLevelsThisTrial.append(patient.update());
            ResistPopListThisTrial.append(patient.getResistPop(['guttagonol']));

        for i in range(len(ResistPopListThisTrial)):
            tempResistPopList.append(ResistPopListThisTrial[i]);

        return virusLevelsThisTrial;
    accumulatedVirusLevels = [];
    virusLevelResults = [];
    resistPopList = [];

    for trial in range(numTrials):
        tempResistPopList = [];
        virusLevelResults = runTrialDrug(300, numViruses, maxPop, maxBirthProb, clearProb, resistances.copy(), mutProb, tempResistPopList);

        if trial == 0:
            accumulatedVirusLevels = virusLevelResults;
            resistPopList = tempResistPopList[:];

        else:
            for i in range(len(virusLevelResults)):
                accumulatedVirusLevels[i] += virusLevelResults[i];

            for i in range(len(tempResistPopList)):
                resistPopList[i] += tempResistPopList[i];

    accumulatedVirusLevels.remove(accumulatedVirusLevels[0]);
    resistPopList.remove(resistPopList[0]);

    for i in range(len(accumulatedVirusLevels)):
        accumulatedVirusLevels[i] /= float(numTrials);

    for i in range(len(resistPopList)):
        resistPopList[i] /= float(numTrials);



    pylab.plot(range(0, len(accumulatedVirusLevels)), accumulatedVirusLevels, label = "Total")
    pylab.plot(range(0, len(resistPopList)), resistPopList,
               label = "ResistantVirus")
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("time step")
    pylab.ylabel("# viruses")
    pylab.legend(loc = "best")
    pylab.show()
