## II Basic Terminology

### 1. Classification vs. Regression

Given a training set \(X_l = \{(x_i, y_i)\} \) for \(i = 1, 2, ..., l\):
- \(x_i\): Objects or feature vectors residing in an n-dimensional real space (often referred to as the feature space) represented as \(ℝ^n\).
- \(y_i\): Responses or target variables corresponding to each \(x_i\).

### 2. Classification

Classification is the task where data points are categorized into predefined categories or classes.

- **Output Space**: \(Y = \{-1, 1\}\). In binary classification, each data point \(x_i\) is assigned to one of two classes, either -1 or +1.
  
- **Algorithm (or model)**: 
  `a(x, w) = sign(w . x_i)`
  The prediction for a data point is based on the sign of the dot product between the weight vector \(w\) and the data point \(x_i\).

- **Loss Function**: 
  `Q(w; X_l) = sum for i=1 to l of Indicator[w . x_i y_i < 0]`
  A cumulative measure of how often the model made an incorrect prediction. The objective is to minimize this loss.

### 3. Regression

Regression predicts a continuous value, not a class label.

- **Output Space**: \(Y = ℝ\). This means the output is a real number.

- **Algorithm (or model)**: 
  `a(x, w) = w . x_i`
  The prediction for a data point is the dot product between the weight vector \(w\) and the data point \(x_i\).

- **Loss Function**: 
  `Q(w; X_l) = sum for i=1 to l of (w . x_i - y_i)^2`
  This is the sum of squared differences between the predicted values and the actual values, and the goal is to minimize this loss.

**Summary**:
- **Classification**: Predicts which category or class a data point belongs to.
- **Regression**: Predicts a continuous value for a data point.
