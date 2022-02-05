## Forward and Backwards Errors

You might assume that scientific computing consists of the process:  

Problem formulated mathematically $\Rightarrow$ algorithm $\Rightarrow$ solution.  

Implicit in this is the assumption that all mathematically formulated problems have meaningful solutions.  You might be surprised to learn that this is not actually the case.

### Example: A poorly conditioned problem

Consider the initial value problem  

$$ \frac{dx}{dt}-x=e^{-2t}, \qquad x(0)=-\frac{1}{3}.$$

It is straightforward to verify (by plugging it in the above equation) that the exact solution to this problem is  

$$x(t)=-\frac{e^{-2t}}{3}.$$

However, if we *perturb* the initial value by a small number $\epsilon$, so that $\tilde{x}(0)=-\frac{1}{3}+\epsilon$ the exact solution is now

$$\tilde{x}(t)=\epsilon e^{+t}-\frac{e^{-2t}}{3}.$$

After a short time $t$ the first term will dominate the second no matter how small $\epsilon$ is (assuming it is non-zero).  Also, consider that $x(0)=-1/3=-0.33333...$ cannot be represented exactly on a computer so we would never be able to recover the exact solution numerically, independent of whatever algorithm you might attempt to use.

We refer to problems like this as *ill-conditioned* problems.  Meaning that small changes (perturbations) in the input data (problem formulation) cause large changes in the resulting solution.  To quantify this further it is useful to consider the following:  

- **backward error, $E_b$**:  This is what we use to quantify how close our formulation of the problem is to the true problem we are trying to solve, or more precisely, how close our approximate solution comes to solving the true problem.

- **forward error, $E_f$**:  This quantifies how close the solution we find is to the solution to the true problem we are trying to solve.  

- **condition number**, $\mathcal{C}=\frac{E_f}{E_b}$.

Note that these definitions are not precise in the sense that they leave a few choices open, such as whether $E_f$ and $E_b$ are absolute or relative errors.  However, independent of this choice, a larger condition number $\mathcal{C}$ indicates a more poorly conditioned problem.  As such, the relative magnitude of $\mathcal{C}$ can be used to evaluate different formulations of a given mathematical problem to decide which formulation is better conditioned.

In our example above where we solve the differential equation analytically, the perturbed solution $\tilda{x}(t)$ satisfies the differential equation exactly so the only source of backward error here is the initial condition so $E_b=\epsilon$.  The forward error is also fairly straightforward as $E_f = |x(t)-\tilde{x}(t)| = \epsilon e^t$.  So here we see the condition number

$$\mathcal{C} =  \frac{E_f}{E_b} = e^t.$$

The condition number here grows with time.  What this means is that if we refine our question to something like: What is $x(T)$ for $T=0.5$?  The condition number for this more precise problem is $\mathcal{C}=e^{0.5}\approx 1.64$ which makes this a reasonable question to ask (i.e. is reasonably well-conditioned).  However, if you ask the question: What is $x(T)$ for $T=25$? then the condition number is $\mathcal{C}=e^{25} \approx 7\times 10^{10}$ which is a very poorly conditioned problem, meaning it is not really a question you can give a meaningful answer to.

### Example: Conditioning for linear systems

Suppose you want to solve the problem

$$\mathbf{A}\mathbf{x}=\mathbf{b}.$$

Where we will assume $\mathbf{A}$ is a $n\times n$ matrix, $\mathbf{x}$ is the unknown we are trying to find and is a $n\times 1$ column vector, and $\mathbf{b}$ is a known $n\times 1$ column vector.  Unless $\mathbf{A}$ and $\mathbf{b}$ are a special form of matrices with particular choices of rational numbers for their entries, we cannot usually solve this problem exactly.  In other words, due to issues such as finite precision and other problems we will discuss in more detail in a later chapter, we can only find an approximation to our solution which we will call $\tilde{\mathbf{x}}$.  In this case it is fairly clear the absolute *forward* error would be  

$$E_f=||\mathbf{x}-\tilde{\mathbf{x}}||$$

where $||\cdot||$ indicates a suitable vector norm (for error estimates it is usually sufficient to just use the $\infty$-norm, the absolute value of the largest element in magnitude). The absolute *backward* error is just the measure of how well our approximate solution solves the exact formulation of the problem,  

$$E_b=||\mathbf{A} \tilde{\mathbf{x}}-\mathbf{b}||.$$  

Note, however, that we can also consider $\tilde{\mathbf{x}}$ to be the exact solution to a different, but "nearby" problem  

$$\mathbf{A}\tilde{\mathbf{x}}=\tilde{\mathbf{b}}$$  

and this means that the backward error  

$$E_b=||\mathbf{A} \tilde{\mathbf{x}}-\mathbf{b}||=||\tilde{\mathbf{b}}-\mathbf{b}||$$  

is a measure of how "close" this nearby problem is to the original problem we set out to solve.

The condition number for linear systems is usually defined in terms of relative errors so for this problem it would be

$$\mathcal{C} = \frac{\frac{||\mathbf{x}-\tilde{\mathbf{x}}||}{||\mathbf{x}||}}{\frac{||\tilde{\mathbf{b}}-\mathbf{b}||}{||\mathbf{b}||}}.$$

One thing you may have already realized is that we would not normally be able to compute the forward error for our problem (because we do not know the exact solution).  However, the backward error *is* easily computed.  As a result, we can often compute the backward error and then, using an estimate of an upper bound for the condition number, estimate a bound for our forward error.


### Stability

Suppose we are given a well-conditioned problem, then a **stable algorithm** is one that preserves this property (i.e. small changes in the problem data formulation *and* application of our algorithm result in small changes to our approximate solution).  Conversely, an **unstable algorithm** is one where, given a well-conditioned problem, small errors in the problem data and application of the algorithm gives large changes in the approximate solution.  Typically, a stable algorithm is one that gives us a numerically exact solution to a problem that is nearby (in the backward error sense) to our original problem.

When you encounter what appears to a large condition number (it is usually fairly obvious is small changes to input result in huge changes to output), it is very important to undersand whether the issue is due to poor conditioning of the underlying problem or application of an unstable algortihm.  Applying a stable algorithm to a poorly conditioned problem will give very similar results to applying an unstable algorithm to a well conditioned problem.  The solution is *very* different for these two cases.  In the case where the underlying problem is poorly conditioned you are *asking the wrong question* and need to think hard about what the right question would be.  If the problem is well conditioned but the algorithm is unstable there may be algorithmic parameter that could be adjusted (such as making a step size smaller) or perhaps a completely different algorithm is needed.

In algorithms that involve a large number of repeated steps, such as integrating a differential equation forward in time, it is clear that the absolute error will inevitably grow with time as errors accumulate.  As a rule of thumb, if the input error is $\epsilon$ and after $n$ steps the error is $E_n$ then  

- if $E_n \approx C n \epsilon$ where C is constant, then the algorithm is stable,

- if $E_n \approx k^n \epsilon$ with $k>1$ then the algorithm is unstable.






