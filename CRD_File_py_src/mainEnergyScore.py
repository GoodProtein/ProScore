import math
import time
import EnergyScoreMethods

def energyScoreTest():
    inputFilePath1 = "../data/model1.crd"
    inputFilePath2 = "../data/model2.crd"
    outputFilePath1 = "../results/protein1Atoms.csv"
    outputFilePath2 = "../results/protein2Atoms.csv"
    # process protein #1
    runtimeProfile1 = EnergyScoreMethods.RuntimeProfile()
    atomMap1 = EnergyScoreMethods.atomMapFromCRD(inputFilePath1, runtimeProfile1)
    print("Protein #1 file processing time:",
          runtimeProfile1.getDurationMS(), "milliseconds")
    # Uncomment next line to debug hash table structure
    EnergyScoreMethods.atomMapToCSV(atomMap1, outputFilePath1)
    # process protein #2
    runtimeProfile2 = EnergyScoreMethods.RuntimeProfile()
    atomMap2 = EnergyScoreMethods.atomMapFromCRD(inputFilePath2, runtimeProfile2)
    print("Protein #2 file processing time:",
          runtimeProfile2.getDurationMS(), "milliseconds")
    # Uncomment next line to debug hash table structure
    EnergyScoreMethods.atomMapToCSV(atomMap2, outputFilePath2)
    # calculate protein #1
    runtimeProfile3 = EnergyScoreMethods.RuntimeProfile()
    energyScore1 = EnergyScoreMethods.calculateEnergyScore(atomMap1, runtimeProfile3)
    print("Protein #1 calculate internal energy processing time:",
          runtimeProfile3.getDurationMS(), "milliseconds")
    print("The internal energy of the protein #1 is",
          int(round(energyScore1)), "kcal/mol")
    # calculate protein #2
    runtimeProfile4 = EnergyScoreMethods.RuntimeProfile()
    energyScore2 = EnergyScoreMethods.calculateEnergyScore(atomMap2, runtimeProfile4)
    print("Protein #2 calculate internal energy processing time:",
          runtimeProfile4.getDurationMS(), "milliseconds")
    print("The internal energy of the protein #2 is",
          int(round(energyScore2)), "kcal/mol")
    # Protein comparison
    if(energyScore1 < energyScore2):
        print(
            "The energy score of the protein #1 is less, so it is more likely to occur")
    else:
        print(
            "The energy score of the protein #2 is less, so it is more likely to occur")

if __name__ == "__main__":
    energyScoreTest()
