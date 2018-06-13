# Naive Bayes
  ## Concept
  In an ideal world the value of any give feature would be totally independent
  from the value of another feature for a data point. If this were the case we
  could use Bayes Law/Rule to compute the missing value or to be predicted
  value after working out the subsequent relationship between the features. 
  As it stands however this is not the case, and frequently there are complex
  underlying relationships in our data that are impossible to model on
  computers. It can, however, be useful to pretend that these relationships
  are independent and apply Bayes Law anyway. This is where Naive Bayes comes
  in!
  ## Math Involved
  * Bayes Rule
    Let $x = (x_1, x_2, ..., x_n)$ \\
    $p(C_k | x) = \frac{p(C_k)p(x|C_k)}{p(x)}\\
    (Read $p(y|x)$ as the probability of y given that x has occured)
  * Naive Bayes Assumption
    $C_k = argmax p(C_k)\prod_{i=1}^{n}p(x_i|C_k)$ 

