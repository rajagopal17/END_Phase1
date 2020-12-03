# Week 6 - LSTM, GRUs, Seq2Seq or Encoder-Decoder Architecture and Attention Mechanism

This assignment is based on the Week6 class and gives some intuition behind LSTM, GRU and Attentions

## Group Members
* Anubhab Panda (pandaanubhav@gmail.com)
* Sachin Dangayach (sachin.dangayach@gmail.com)


## Assignment Instructions

Write a Linkedin/Medium Blog that explains LSTM, GRU and Attention Block (not the whole attention mechanism, just the discussion we had on [s0, h1, h2, h3]. MUST INCLUDE SELF DRAWN (on some software or hand-drawn) IMAGE.

## BlogPost on LSTM, GRU and Attention Mechanism

This blog gives an intuitive and visual explanation on the inner workings of LSTM, GRU and Attention. This blog has been inspired by [Chris Olah's blogpost on LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) and [Jay Alammar's blogpost on Attentions](http://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/).
Without further ado let's dig deep.

# LSTM (Long Short Term Memory)

To understand LSTM, we first have to look at RNN and their shortcomings. A Recurrent Neural Network is a network with a loop. It processes information sequentially and the output from every time step is fed back to the network which acts as a sort of memory. This feedback is called as hidden state. The output from a RNN cell is the final hidden state.

<p align="center">
    <img src="https://github.com/anubhabPanda/END_Phase1/blob/main/Week6/Images/RNN.gif" width = "400px">
</p>

But the main shortcoming of RNN is its limited memory. For e.g. If we are trying to predict the sentiment based on customer reviews and our review is something like this -  
*I like this product.........Due to one of the bad features, this product could have been better.*    

Since our review is very long, the RNN will only have access to the recent part of the sequence due to its limited memory hence it will say that this review is negative but infact this review is a neutral one as the user initially says that he liked the product.  
This limited memory occurs due to vanishing gradients. When we are backpropagating, when the sequence is long, initial layers of RNN are not able to learn due to this problem.

LSTM's overcomes this shortcoming partially by maintaining a context vector which is like a highway. The context vector has an easier back propagation path hence it overcomes the vanishing gradient problem. Let's look at how LSTM works

<p align="center">
    <img src="https://github.com/anubhabPanda/END_Phase1/blob/main/Week6/Images/LSTM_1.png" width = "1280px">
</p>

Let's look at a LSTM cell and see the steps that occurs inside it.

* The Cell State C<sub>t</sub> acts like a memory and retains the context information.
* First the hidden state vector from previous cell h<sub>t-1</sub> is concatenated with the input vector X<sub>t</sub> . Let's call this NX<sub>t</sub>
* **Forget Gate(1)** : The concatenated vector NX<sub>t</sub> then passes through the forget gate (1). The forget gate is a sigmoid gate which squishes the concatenated vector between 0 and 1. Whatever information is to be added to the context vector is pushed towads 1 while the information that is to be forget is pushed towards zero. The output from the sigmoid gate is multiplied with the context vector from the previous time step.  
    Let the output from the sigmoid be denoted as f<sub>t</sub>. After C<sub>t-1</sub> is multiplied elementwise by f<sub>t</sub> we get C<sub>t*</sub>
<p align="center">
    <img src="https://github.com/anubhabPanda/END_Phase1/blob/main/Week6/Images/forget_gate.PNG" width = "400px">
</p>

* **Input Gate(2)** : The concatenated vector NX<sub>t</sub> is passed through the sigmoid gate(2). The output of this let's denote with i<sub>t</sub>. The sigmoid gate squishes the information between 0 and 1. The information to be retained is pushed towards 1 and information to be forgotten is pushed towards 0. Since this information is to be used with Gate Gate output to add to the context vector C<sub>t*</sub>, backpropagation decides the weight accordingly, such that the required information is retained.
<p align="center">
    <img src="https://github.com/anubhabPanda/END_Phase1/blob/main/Week6/Images/input_gate.PNG" width = "400px">
</p>

* **Gate Gate(3)** : The concatenated vector NX<sub>t</sub> is passed through the tanh gate(3). The output of this let's denote with g<sub>t</sub> tanh gate squishes the input between -1 and 1 and prevents the number from becoming very large. This helps in calculation as well as the number from blowing up.
<p align="center">
    <img src="https://github.com/anubhabPanda/END_Phase1/blob/main/Week6/Images/gate_gate.PNG" width = "400px">
</p>

* i<sub>t</sub> is multiplied elementwise with g<sub>t</sub> to attain new candidate values for the Cell state C<sub>t*</sub>. This candidate value is added elementwise with the C<sub>t*</sub> vector and we get the new context vector C<sub>t</sub>.
<p align="center">
    <img src="https://github.com/anubhabPanda/END_Phase1/blob/main/Week6/Images/New_Cell_State.PNG" width = "400px">
</p>

* **Output Gate(4)** : The concatenated vector NX<sub>t</sub> is passed through sigmoid gate so that the information that are to be passed to the output vector is retained by pushing it towards 1 and information that is not be passed to the output vector is pushed towards 0. The context vector C<sub>t</sub> is passed through tanh gate to have values between -1 and 1 and the output of this is multiplied elementwise with the output from the sigmoid gate to get the new hidden state vector.
<p align="center">
    <img src="https://github.com/anubhabPanda/END_Phase1/blob/main/Week6/Images/Final_Hidden.PNG" width = "1280px">
</p>

* The final hidden state is the output vector incase of single output after all timesteps. In situation where every timestep requires an output , the hidden state from each timestep is considered as an output. In LSTM the long term memory is achieved through the context vector while the short term memory is achieved through the hidden state.  

Some of the shortcomings of LSTMs:

* LSTMs take longer to train
* LSTMs require more memory to train
* LSTMs are easy to overfit
* Dropout is much harder to implement in LSTMs

# GRU (Gated Recurrent Unit)

The workings of the GRU are similar to LSTM. Since the workings of the forget gate and input gate are opposite to each other, GRU combines both gates into a single update gate.

It also combines the hidden state vector and the context vector into a single vector.
<p align="center">
    <img src="https://github.com/anubhabPanda/END_Phase1/blob/main/Week6/Images/GRU.PNG" width = "1280px">
</p>

# Encoder Decoder Architecture with Attention

An Encoder Decoder Architecture consists of two parts. The encoder is a series of LSTM/GRU cells. The output from the encoder is passed to the decoder which also is a series of LSTM cells.

<p align="center">
    <img src="https://github.com/anubhabPanda/END_Phase1/blob/main/Week6/Images/Encoder_Decoder.PNG" width = "1280px">
</p>

In order to improve the performance of the model further and to improve the context vector we introduce another step between the encoder and decoder cells called Attention. 

Steps for calculating the attention weights: 
* all hidden states from the encoder (h<sub>t-2</sub>, h<sub>t-1</sub> and h<sub>t</sub>) and the hidden state of previous time step from the decoder (s<sub>t-2</sub>) is concatenated into a single vector.
* the concatenated vector is passed through a fully connected layer to get a new vector. This vector is passed throgh the softmax activation.
* This vector is multiplied with softmax vector and summed up to get final attention scores.
* During decoding, the context vector is multiplied with the hidden state/cell state to get the final output.

<p align="center">
    <img src="https://github.com/anubhabPanda/END_Phase1/blob/main/Week6/Images/Encoder_Decoder_Attention.PNG" width = "1280px">
</p>