# NeuroEvol-WordGen
![Working Gif](<PlaceHolder>)
**Project duration**: 3 to 5 days  
**IDE**: Pycharm 2019.2.3 (Community Edition)  
**Python Version**: Python 3.7


## Description
The infinite monkey theorem states 'that a monkey hitting keys at random on a typewriter for an infinite amount of time will surely type a given text, such as the complete works of William Shakespeare. However, the probability of such a thing occuring is so small that the chance of it occurring during a period of time hundreds of thousands of orders of magnitude longer than the age of the universe is extremely low (but technically not zero).


The following code is a NeuroEvolution genetic algorithm that "breeds" the smartest monkeys from each population until a monkey smart enough can generate a given phrase.


## How it works
1. The setup() function generates random words that are the same length as the target word

2. The fitness of each word is calculated using the DNA.CalculateFitness() function. This checks each letter in a randomly generated word against it's corresponding letter in the target word.

3. Once the fitness is calculated, each word (if it has atleast 1 fitness) is added to the mating pool in a manner consistent with it's fitness.

    - **Fitness Function 1:** A linear relationship between the fitness and the probability of being selected for breeding.
    
    - **Fitness Function 2:** An exponential relationship between the fitness and the probability of being selected for breeding.
    
4. From the mating pool two parents are randomly selected, bred, and their resulting child possibly mutated. The population variable is then cleared, and each new child is then appended to the population variable. Where each child is closer to the target word than it's parents. And hence, each population contains DNA objects that are closer to the target word.

    - **Breeding Process:** A random point is selected in each parent's word. For ParentA the first halve is selected for breeding and for ParentB the second halve is selected for breeding. As a result the child formed contains the first halve of ParentA and the second halve of ParentB.
    ![Breeding](<PlaceHolder>)
    
     - **Mutation Process:** A random point number in the range 0 to 1 is generated, if this number is lower than the mutation rate given by the user - each letter of the child is checked. If it is incorrect, it is replaced by another random letter.
     ![Mutation](<PlaceHolder>)

5. Repeat steps 2 to 4 until the target word is generated.
    

## Getting Started

1. Clone this repo using the following command  
```
$ git clone https://github.com/Zafirmk/NeuroEvol-WordGen.git
$ cd NeuroEvol-WordGen
```
2. Open the project in your preferred IDE  

3. Edit the string library so that lower case ascii contains a ' ' (ie: Spacebar)

### Prerequisites
Things you need to install before running:
*  [Python](https://www.python.org/)
*  [Numpy](https://www.numpy.org/)

#### Additional Notes
*  All images obtained from [The Nature of Code by Daniel Shiffman](https://www.natureofcode.com/)
