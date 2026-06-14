## **Q. Introduction to Neural Networks** 

## A. **1. What is a Neural Network?** 

An **Artificial Neural Network (ANN)** is a machine learning model inspired by the structure and working of the human brain. 

It consists of interconnected processing units called **neurons** , which work together to solve problems such as: 

- Image Recognition 

- Speech Recognition 

- Language Translation 

- Medical Diagnosis 

- Fraud Detection 

## **Definition** 

An Artificial Neural Network is a network of artificial neurons that learns patterns from data by adjusting connection weights between neurons. 

## **2. Biological Inspiration** 

ANNs are inspired by the human nervous system. 

The human brain contains billions of neurons connected together. 

Learning occurs when the strength of connections between neurons changes. 

The same idea is applied in Artificial Neural Networks. 

## **Biological Neuron Structure** 

A biological neuron has three major parts: 

## **A. Dendrites** 

- Receive signals from other neurons. 

- Act as input channels. 

## **B. Cell Body (Soma)** 

- Processes incoming information. 

- Contains the nucleus. 

## **C. Axon** 

- Sends processed signals to other neurons. 

## **D. Synapse** 

- Junction between neurons. 

- Transfers signals. 

- Strength of synapse determines learning. 

According to the notes, learning in biological organisms occurs because synaptic strengths change in response to external stimuli. 

## **3. Artificial Neuron** 

Artificial Neural Networks imitate the behavior of biological neurons. 

An artificial neuron receives inputs, processes them, and generates an output. 

## **Components** 

- Inputs (x₁, x₂, x₃ …) 

- Weights (w₁, w₂, w₃ …) 

- Bias (b) 

- Activation Function 

- Output (y) 

## **Biological vs Artificial Neuron** 

|**Biological Neuron**|**Artificial Neuron**|
|---|---|
|Dendrites|Input|
|Cell Body|ProcessingUnit|
|Synapse|Weight|
|Axon|Output|
|Synaptic Strength|Weight Value|



## **4. Why Are Weights Important?** 

Weights determine the strength of a connection. 

## **High Weight** 

Input strongly influences output. 

## **Low Weight** 

Input has little influence. 

Example: Suppose: Input = 10 

Weight = 0.9 

Output influence = 9 Weight = 0.1 Output influence = 1 

Thus, weights decide which inputs are more important. 

## **5. How Does Learning Occur?** 

In biological neurons, Experience changes synaptic strengths. 

In ANN, Training data changes weights. 

Learning means: Adjust weights 

↓ 

Reduce error 

↓ 

Improve predictions 

## **6. Working of a Neural Network** 

The network receives input data. 

Example: Image of banana 

**Step 1** 

Input image is converted into numerical values. 

**Step 2** 

Values are passed through neurons. 

**Step 3** 

Each neuron performs calculations. 

**Step 4** 

Output is generated. 

Example: 

Banana : 0.95 Carrot : 0.03 Apple  : 0.02 

Prediction : Banana 

**Step 5** 

Prediction is compared with actual answer. 

**Step 6** 

Weights are adjusted. 

This process repeats many times. 

## **7. Neural Network Computation** 

The output of a neuron is obtained by multiplying inputs with weights and adding them. 

The weighted sum is: 

z=\sum_{i=1}^{n} w_i x_i+b 

where 

- x = inputs 

- w = weights 

- b = bias 

The result is passed through an activation function to produce the final output. 

## **Q. Basic Architecture of Neural Networks** 

A. An **Artificial Neural Network (ANN)** is a computational model inspired by the human brain. It consists of interconnected neurons arranged in layers that process information and learn patterns from data. The architecture of a neural network refers to the arrangement of neurons, layers, and connections between them. 

**Architecture of a Neural Network** 

A neural network is generally organized into three types of layers: 

Input Layer 

↓ 

Hidden Layer(s) 

↓ 

Output Layer 

The network is structured as a **Directed Acyclic Graph (DAG)** , where information flows only in the forward direction from input to output. 

## **1. Input Layer** 

- The input layer receives data from the external environment. 

- Each neuron in this layer represents one input feature. 

- It does not perform any computation; it only passes data to the next layer. 

Example: 

- House price prediction: 

   - Area 

   - Number of bedrooms 

   - Age of house 

These features are fed into the input layer. 

## **2. Hidden Layer** 

- The hidden layer lies between the input and output layers. 

- It performs computations using weights, biases, and activation functions. 

- Hidden layers extract useful features and learn complex relationships from data. 

- A neural network may contain one or more hidden layers. 

The use of hidden layers significantly increases the learning capability of the network. 

## **3. Output Layer** 

- The output layer produces the final prediction or result. 

- The number of output neurons depends on the problem. 

Examples: 

- Binary Classification → 1 output neuron 

- Multi-class Classification → Multiple output neurons 

- Regression → 1 numerical output neuron 

## **Weights and Bias** 

## **Weights** 

- Connections between neurons contain weights. 

- Weights determine the importance of each input. 

- Learning occurs by adjusting these weights. 

## **Bias** 

- A bias neuron always outputs 1. 

- Bias helps shift the activation function and improves model flexibility. 

- Bias neurons can be used in hidden as well as output layers. 

## **Single-Layer Neural Network (Perceptron)** 

The simplest neural network is called a **Perceptron** . 

Characteristics: 

- Contains only one computational layer. 

- No hidden layer. 

- Suitable for linearly separable problems. 

- Performs binary classification. 

## **Multilayer Neural Network** 

A multilayer neural network contains one or more hidden layers between the input and output layers. 

Characteristics: 

- Learns complex and non-linear patterns. 

- Has higher learning capacity. 

- Used in modern deep learning applications. 

- Hidden layers perform intermediate computations. 

This architecture is called a **Feed-Forward Neural Network** because information flows only in the forward direction. 

## **Feed-Forward Process** 

The operation of a neural network follows these steps: 

1. Inputs are provided to the input layer. 

2. Inputs are multiplied by weights. 

3. Bias is added. 

4. Activation function is applied. 

5. Results are passed to the next layer. 

6. Final output is generated. 

This process is called **Forward Propagation** . 

**Advantages of Multilayer Architecture** 

1. Learns complex patterns. 

2. Handles non-linear problems. 

3. Provides better prediction accuracy. 

4. Improves generalization ability. 

5. Forms the foundation of deep learning. 

## **Q. Perceptron Model** 

## A. **Introduction** 

The **Perceptron** is the simplest form of an Artificial Neural Network (ANN). It was proposed by **Frank Rosenblatt** and is used for **binary classification problems** . A perceptron 

consists of an input layer and an output neuron, where inputs are multiplied by weights, summed together with a bias, and passed through an activation function to produce the output. 

## **Architecture of a Perceptron** 

The perceptron consists of: 

- Input Nodes (x₁, x₂, …, xₙ 

- Weights (w₁, w₂, …, wₙ) 

- Bias (b) 

- Summation Unit 

- Activation Function 

- Output Node 

**Working of a Perceptron** 

## **Step 1: Input Layer** 

The input layer receives feature values: 

X = [x1, x2, x3, ..., xn] 

The input layer only transmits data and performs no computation. 

**Step 2: Weighted Sum** 

Each input is multiplied by its corresponding weight and added together along with a bias. The net input is: 

z=\sum_{i=1}^{n}w_ix_i+b 

where: 

- x ᵢ = Input 

- w ᵢ = Weight 

- b = Bias 

## **Step 3: Activation Function** 

The perceptron uses the **Sign Activation Function** . 

Output is calculated as: 

y=sign(z) 

Decision Rule: 

If z ≥ 0  → y = +1 

## If z < 0  → y = -1 

This makes the perceptron suitable for binary classification. 

## **Bias in Perceptron** 

Bias acts like the intercept term in a linear equation. 

Functions of bias: 

- Increases flexibility of the model 

- Shifts the decision boundary 

- Allows activation even when all inputs are zero 

A bias neuron always transmits a value of 1, and its associated weight acts as the bias term. 

## **Perceptron Learning Algorithm** 

The perceptron learns by adjusting weights based on prediction error. 

## **Steps** 

1. Initialize weights randomly. 

2. Feed input data to the perceptron. 

3. Calculate the output. 

4. Compare predicted output with actual output. 

5. Compute error. 

6. Update weights. 

7. Repeat until convergence. 

## **Error Calculation** 

The prediction error is: 

e=y-\hat{y} 

where: 

- y = Actual output 

- ŷ = Predicted output 

If error is non-zero, weights must be updated. 

## **Weight Update Rule** 

The perceptron updates weights using: 

w_{new}=w_{old}+\alpha(y-\hat{y})x 

where: 

- α = Learning Rate 

- x = Input 

- y = Actual Output 

- ŷ = Predicted Output 

The learning rate controls the magnitude of weight updates. 

## **Epoch** 

An **Epoch** is one complete pass through all training examples in the dataset. 

Example: 

- Dataset contains 100 samples. 

- Processing all 100 samples once = 1 Epoch. 

Training usually requires multiple epochs until the network converges. 

## **Linear Separability** 

The perceptron can successfully classify data only when it is **linearly separable** . 

## **Linearly Separable Data** 

A straight line (or hyperplane) can separate the classes. 

Decision boundary: 

W^TX+b=0 

## **Non-Linearly Separable Data** 

Example: 

- XOR Problem 

A single perceptron cannot solve XOR because the classes cannot be separated using one straight line. 

## **Perceptron Convergence Theorem** 

The Perceptron Convergence Theorem states that: 

## **If the training data is linearly separable, the perceptron algorithm is guaranteed to converge and achieve zero training error after a finite number of iterations.** 

## **Advantages of Perceptron** 

1. Simple and easy to implement. 

2. Fast training process. 

3. Suitable for binary classification. 

4. Requires less computational power. 

5. Foundation for advanced neural networks. 

## **Limitations of Perceptron** 

1. Works only for linearly separable data. 

2. Cannot solve XOR problems. 

3. Limited learning capability. 

4. Single-layer architecture. 

## **Q. Activation Functions** 

## A. **Introduction** 

An **Activation Function** is a mathematical function applied to the weighted sum of inputs and bias of a neuron. It determines whether a neuron should be activated and what output should be passed to the next layer. The primary purpose of an activation function is to introduce **non-linearity** into the neural network, enabling it to learn complex patterns and relationships in data. 

## **Need for Activation Functions** 

Without activation functions, a neural network behaves like a simple linear model regardless of the number of layers. 

Advantages of activation functions: 

1. Introduce non-linearity. 

2. Enable learning of complex patterns. 

3. Improve prediction accuracy. 

4. Allow deep neural networks to solve real-world problems. 

5. Help in classification and regression tasks. 

## **Working of an Activation Function** 

First, a neuron computes the weighted sum: 

z=\sum_{i=1}^{n}w_ix_i+b 

where: 

- x ᵢ = Inputs 

- w ᵢ = Weights 

- b = Bias 

The activation function is then applied: 

Output = f(z) 

The value before activation is called the **pre-activation value** , and the value after activation is called the **post-activation value** . 

## **Types of Activation Functions** 

## **1. Linear (Identity) Activation Function** 

The output is equal to the input. 

## **Characteristics** 

- No non-linearity. 

- Used mainly in output layers. 

- Suitable for regression problems. 

## **Applications** 

- House Price Prediction 

- Temperature Forecasting 

## **2. Sign Activation Function** 

Used in perceptrons for binary classification. 

Rule: 

If x ≥ 0 → +1 

If x < 0 → -1 

## **Characteristics** 

- Produces binary outputs. 

- Non-differentiable. 

- Not suitable for gradient-based learning. 

## **Application** 

- Perceptron Model 

## **3. Sigmoid Activation Function** 

Maps input values to the range (0,1). 

## **Characteristics** 

- Smooth and differentiable. 

- Produces probability values. 

- Commonly used in binary classification. 

## **Advantages** 

- Easy interpretation as probability. 

- Differentiable. 

## **Disadvantages** 

- Suffers from vanishing gradient problem. 

## **Application** 

- Binary Classification 

## **4. Tanh Activation Function** 

A scaled version of the sigmoid function. 

tanh(x)=\frac{e^{2x}-1}{e^{2x}+1} 

## **Characteristics** 

- Output range: (-1,1) 

- Zero-centered. 

- Better learning than sigmoid. 

## **Advantages** 

- Faster convergence than sigmoid. 

## **Disadvantages** 

- Still affected by vanishing gradients. 

## **Application** 

- Hidden Layers (older neural networks) 

## **5. ReLU (Rectified Linear Unit)** 

The most widely used activation function in modern neural networks. 

f(x)=max(0,x) 

## **Working** 

If x > 0 → Output = x 

If x ≤ 0 → Output = 0 

## **Advantages** 

1. Computationally efficient. 

2. Avoids vanishing gradients. 

3. Enables deep learning. 

4. Faster training. 

## **Disadvantages** 

- Dead ReLU problem. 

## **Applications** 

- Hidden Layers 

- CNNs 

- Deep Learning Models 

## **6. Softmax Activation Function** 

Used for multiclass classification problems. 

For k classes: 

P_i=\frac{e^{v_i}}{\sum_{j=1}^{k}e^{v_j}} 

## **Characteristics** 

- Converts outputs into probabilities. 

- Sum of all probabilities equals 1. 

## **Applications** 

- Image Classification 

- Digit Recognition 

- Language Processing 

## **Choice of Activation Functions** 

According to the application: 

- **Regression** → Linear Activation 

- **Binary Classification** → Sigmoid Activation 

- **Multi-class Classification** → Softmax Activation 

- **Hidden Layers** → ReLU Activation 

- **Output Range (-1,1)** → Tanh Activation 

## **Q. Loss Functions, Multilayer Networks & Backpropagation** 

## A. **Introduction** 

Artificial Neural Networks learn by minimizing prediction errors. The error is measured using **Loss Functions** , complex problems are solved using **Multilayer Neural Networks** , 

and learning is achieved through the **Backpropagation Algorithm** . Together, these concepts form the foundation of modern neural network training. 

## **1. Loss Functions** 

A **Loss Function** measures the difference between the actual output and the predicted output of a neural network. It indicates how well or poorly the model is performing. 

## **Importance of Loss Functions** 

- Measures prediction error. 

- Guides weight updates. 

- Helps improve model accuracy. 

- Acts as the objective function to be minimized during training. 

## **Types of Loss Functions** 

## **A. Mean Squared Error (MSE)** 

Used mainly for regression problems. 

MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2 

## **Applications:** 

- House Price Prediction 

- Temperature Forecasting 

## **Advantages:** 

- Easy to compute 

- Differentiable 

## **B. Mean Absolute Error (MAE)** 

Measures the average absolute difference between actual and predicted values. 

## **Applications:** 

- Regression Problems 

## **Advantage:** 

- Less sensitive to outliers than MSE 

## **C. Cross Entropy Loss** 

Used for classification tasks. 

For multiclass classification: 

Loss=-\log(P_r) 

where P_r is the probability of the correct class. 

**Applications:** 

   - Image Classification 

   - Disease Prediction 

   - Digit Recognition 

- Cross Entropy is commonly used with Softmax activation. 

## **2. Multilayer Neural Networks** 

A **Multilayer Neural Network (MLNN)** contains one or more hidden layers between the input and output layers. 

**Architecture** 

Input Layer 

↓ 

Hidden Layer(s) 

↓ 

Output Layer 

## **Components** 

## **Input Layer** 

- Receives input features. 

- Performs no computation. 

## **Hidden Layer(s)** 

- Performs intermediate computations. 

- Learns patterns and relationships from data. 

## **Output Layer** 

- Produces final predictions. 

Examples: 

- Classification → Class labels 

- Regression → Numerical values 

## **Feed Forward Neural Network** 

Multilayer neural networks are also called **Feed Forward Networks** because information flows only in the forward direction: 

Input → Hidden → Output 

No cycles or loops exist in the network. 

## **Advantages of Multilayer Networks** 

1. Solve non-linear problems. 

2. Learn complex patterns. 

3. Higher prediction accuracy. 

4. Better generalization. 

5. Foundation of Deep Learning. 

## **3. Backpropagation** 

## **Definition** 

Backpropagation (Backward Propagation of Errors) is the learning algorithm used to train multilayer neural networks. It computes gradients of the loss function and updates weights to minimize error. 

## **Need for Backpropagation** 

In multilayer networks, the loss depends on many layers of weights, making direct optimization difficult. 

Backpropagation solves this problem by: 

- Computing gradients efficiently. 

- Updating weights systematically. 

- Reducing prediction error. 

It uses the **Chain Rule of Differential Calculus** 

## **Phases of Backpropagation** 

Backpropagation consists of two phases: 

## **1. Forward Phase** 

## **Steps** 

1. Inputs are fed into the network. 

2. Outputs of hidden layers are computed. 

3. Final output is generated. 

4. Loss is calculated. 

Input 

↓ 

Hidden Layer 

## ↓ 

Output 

↓ 

Loss 

## **2. Backward Phase** 

## **Steps** 

1. Start from the output layer. 

2. Compute gradients using the chain rule. 

3. Propagate errors backward. 

4. Calculate gradients for all weights. 

5. Update weights. 

Loss 

↑ 

Output Layer 

↑ 

Hidden Layer 

↑ 

Input Layer 

## **Weight Update Rule** 

Weights are updated using Gradient Descent: 

W_{new}=W_{old}-\alpha \frac{\partial E}{\partial W} 

where: 

- W = Weight 

- E = Error 

- \alpha = Learning Rate 

The objective is to minimize the loss function and improve prediction accuracy. 

## **Advantages of Backpropagation** 

1. Efficient learning algorithm. 

2. Works with multilayer networks. 

3. Reduces prediction errors. 

4. Supports deep learning models. 

5. Optimizes weights automatically. 

