# Week 8 - Hands On (II)

This assignment is based on the Week8 class and gives some practise on Neural Machine Translation using Seq2Seq

[![Open Jupyter Notebook](Images/nbviewer_badge.png)](https://nbviewer.jupyter.org/github/anubhabPanda/END_Phase1/blob/main/Week8/S8_Assignment_Solution_Part1.ipynb)


## Group Members
* Anubhab Panda (pandaanubhav@gmail.com)
* Sachin Dangayach (sachin.dangayach@gmail.com)
* Sairam Subramaniam (sairam.subramaniam@gmail.com)
* Amal Mathew (amalmathew246@gmail.com)

## Assignment Instructions

**Part 1:**

1. Look at the [code](https://colab.research.google.com/drive/1VfRlAztiR5UBO9vqoWjoF_U7zWpr8lAZ?usp=sharing) we covered today. Change the languages from german->english to french->german (if you are not comfortable in using raw data in github for french, then change german->english to english->german translation)
2. Change the model such that it has 3 layers instead of 2
3. Train the model on Colab, upload to Github and share the link

**Part 2:**

1. Look at this sample file: [sample.py](https://canvas.instructure.com/courses/2393516/files/120074117/download?wrap=1). You are to write such examples, where you describe the code to be written (starts with #), and the code it should generate. The file shows 3 examples of what text should generate what code. 
2. write 100 such examples. 
3. These are the requirements:
    * if you want the code to print something, then mention "print" in the text
4. read the [sample.py](https://canvas.instructure.com/courses/2393516/files/120074117/download?wrap=1) clearly to see the examples and learn from it. If you want the code to write a program, you are NOT asking to write a function. If you want a function, please mention it.
5. run the code in the terminal/notebook and make sure it runs!
5. you cannot write more than 5 simple functions like add 2/3/4/5 numbers or divide, etc. Try and think of something tough, for example, add a list or tuple together.
6. Stick to python only (no 3rd party library like numpy, etc)
7. here are some examples:
    * provide the length of list, dict, tuple, etc
    * write a function to sort a list
    * write a function to test the time it takes to run a function
    * write a program to remove stop words from a sentence provided,etc

## Part 1 Solution:

### Model Summary
<img src="Images/Model_summary.PNG" height = "200px">

The model has **19,253,679** trainable parameters

### Hyperparameters

* Batch Size: 128
* Epochs: 10
* Loss Function: Cross Entropy Loss
* Optimizer: AdamW
* LR: 0.0001
* Hidden Size: 512 (Both Encoder and Decoder)
* Embedding Dimension: 256 (Both Encoder and Decoder)
* Dropout: 0.5 (Both Encoder and Decoder)
* Number of layers: 3 (Both Encoder and Decoder)

Final Test Set Perplexity of the model is **68.727**

**Solution can be found [here](https://github.com/anubhabPanda/END_Phase1/blob/main/Week8/S8_Assignment_Solution_Part1.ipynb)** 

## Part 2 Solution:

115 code samples were written following the guidelines mentioned above

**Solution can be found [here](https://github.com/anubhabPanda/END_Phase1/blob/main/Week8/S8_Assignment_Solution_Part2.py)**