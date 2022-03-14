(page_topic1)=
Numerical Differentiation
=======================

Suppose we can either evaluate $f(x)$ for any $x$, or are provided with $f(x)$ as some set of points $\{x_i\}_{i=0}^n$, but do not know $f'(x)$.  How do we compute an estimate of $f'(x)$, or $f''(x)$(or higher derivatives, though we will restrict ourselves to the first two derivatives here)?  As always, it is useful to make use of something we already know how to do, namely interpolation.  We replace $f(x)$ with its interpolatory function (Lagrange or splines) and take the derivative of that.  i.e.

$$ f(x) = p(x) + \epsilon(x), $$

where $p(x)$ is our interpolation and $\epsilon(x)$ is the error in the interpolation.  Taking the derivative gives

$$ f'(x) = p'(x) + \epsilon'(x),\qquad f''(x) = p''(x) + \epsilon''(x)$$

Our estimate for the derivative $f'(x) \approx p'(x)$ and $\epsilon'(x)$ is the error in this estimate.  Similarly $f''(x) \approx p''(x)$ and $\epsilon''(x)$ is the error in that estimate. 

In the Lagrange form for the interpolating polynomial, writen in [barycentric form](../InterpFit/BarycentricInterp)  

$$ p_n(x) = \sum_{i=0}^n L_i(x) f(x_i) = \frac{\sum_{i=0}^n \frac{w_i}{x-x_i} f(x_i)}{\sum_{i=0}^n \frac{w_i}{x-x_i}}. $$ (pnformula)

To simplify the notation, we have dropped the $n$ from $L_i^n(x)$ as the appropriate $n$ should be clear from most contexts.  We can see from {eq}`pnformula` that 

$$ p_n'(x) =  \sum_{i=0}^n L_i'(x) f(x_i), \qquad p_n''(x) =  \sum_{i=0}^n L_i''(x) f(x_i)$$

and

$$ L_i(x) =  \frac{\frac{w_i}{x-x_i}}{\sum_{k=0}^n \frac{w_k}{x-x_k}}.$$ (Lieqn)

So to work out the derivative estimates we need to compute $L_i'(x)$ and $L_i''(x)$ for all $i$ (note that these still depend on $n$, but $n$ is the same for all $L_i$ in a given application).

In almost all cases, we are looking for the derivative at a node point, say $x_j$.  To ensure various terms remain differentiable, it is helpful to multiply both sides by $x-x_j$ and rearrange Eq. {eq}`Lieqn` to get

$$ L_i(x)\sum_{k=0}^n w_k \frac{x-x_j}{x-x_k} = w_i\frac{x-x_j}{x-x_i},  $$(Lisetup)

where both sides are now differentiable at $x_j$.  Defining

$$q_j(x)\equiv \sum_{k=0}^n w_k \frac{x-x_j}{x-x_k},$$

we can rewrite {eq}`Lisetup` as

$$ L_i(x)q_j(x) = w_i\frac{x-x_j}{x-x_i},  $$

then take the first and second derivative to get  

$$
\begin{align}
L_i'(x)q_j(x)+L_i(x)q_j'(x)&=w_i \left[\frac{1}{x-x_i}-\frac{x-x_j}{(x-x_i)^2}\right],\\
L_i''(x)q_j(x)+2L_i'(x)q_j'(x)+L_i(x)q_j''(x) &= w_i \left[-2\frac{1}{(x-x_i)^2}+2\frac{x-x_j}{(x-x_i)^3}\right].
\end{align}
$$ (Liderivsetup)

From the definition of $q_j(x)$ one can also work out  

$$
\begin{align}
q_j'(x) &=  \sum_{k\neq j}^n w_k \frac{1}{x-x_k}-\sum_{k\neq j}^n w_k \frac{x-x_j}{(x-x_k)^2},\\
q_j''(x) &= -2\sum_{k\neq j}^n w_k \frac{1}{(x-x_k)^2} + 2\sum_{k\neq j}^n w_k \frac{x-x_j}{(x-x_k)^3}.
\end{align}
$$

For $x_i \neq x_j$, evaluating these at $x=x_j$ we see that  

$$
\begin{align}
q_j(x_j) &= w_j,\\
q_j'(x_j) &= \sum_{k\neq j}^n w_k \frac{1}{x_j-x_k},\\
q_j''(x_j) &= -2\sum_{k\neq j}^n w_k \frac{1}{(x_j-x_k)^2}.
\end{align}
$$

This, along with knowing that $L_i(x_j)=0$, in Eq.{eq}`Liderivsetup` gives for $x_i \neq x_j$,  

$$
\begin{align}
L_i'(x_j)&=\frac{w_i/w_j}{x_j-x_i},\\
L_i''(x_j)&=-2\frac{w_i/w_j}{x_j-x_i}\left[\sum_{k\neq j}\frac{w_k/w_j}{x_j-x_k}+\frac{1}{x_j-x_i} \right].
\end{align}
$$ (DLij)

The $x_i=x_j$ case is more simply obtained from noting that if you interpolate $g(x)\equiv 1$, which can be done exactly (as its derivatives are all zero, the polynomial interpolation error formula says the error is zero), you get $1=\sum_k L_k(x)$.  As a result, by taking derivatives of this expression we get $0=\sum_k L_k^{(m)}(x)$ for each differentiation order $m$.  Hence,

$$
\begin{align}
L_i'(x_i) &= -\sum_{k\neq i} L_k'(x_i),\\
L_i''(x_i) &= -\sum_{k\neq i} L_k''(x_i).
\end{align}
$$ (DLii)

These $L_i^{(m)}(x_j)$ derivatives can be thought of as entries $D_{ji}^{(m)}$ in *differentiation* matrices $\mathbf{D}^{(m)}$.  If we write our known function values $f(x_i)$ in a column vector $\mathbf{F}$ then  $\mathbf{D}^{(m)} F$ provides a column vector of derivatives at the interpolating nodes $x_i$.  Let's illustrate this with a few examples.

**Example: Two point formulas.**  Suppose we have two points $x_0$ and $x_1=x_0+h$ along with the function values at those points $f(x_0)$ and $f(x_1)$.   The [formula for the weights](../InterpFit/BarycentricInterp) gives  $w_0= -1/h$ and $w_1=1/h$.  Eq.{eq}`DLij` then gives

$$ D_{10}'=L_0'(x_1) = -\frac{1}{h},\quad \text{and}\quad D_{01}'=L_1'(x_0)=\frac{1}{h}.  $$

Using these in Eq.{eq}`DLii` gives

$$ D_{00}'=L_0'(x_0) = -\frac{1}{h},\quad \text{and}\quad D_{11}'=L_1'(x_1)=\frac{1}{h}. $$

Using this as the entries of $\mathbf{D}'$ gives

$$
\begin{align}
\left[{\begin{array}{c}
f'(x_0) \\
f'(x_1) \\
\end{array}} \right] \approx
\mathbf{D}'\mathbf{F} =
\left[{\begin{array}{cc}
  -\frac{1}{h} &  \frac{1}{h}\\
  -\frac{1}{h} &  \frac{1}{h}\\
\end{array}} \right]
\left[{\begin{array}{c}
f(x_0) \\
f(x_1) \\
\end{array}} \right] =
\left[{\begin{array}{c}
\frac{f(x_1)-f(x_0)}{h} \\
\frac{f(x_1)-f(x_0)}{h} \\
\end{array}} \right].
\end{align}
$$ (forbackD)

When used for $x_0$ (upper element) this is typically called the *forward* difference formula and when used at $x_1$ (lower element) this is called a *backward* difference.  Not surprisingly as this is based on linear interpolation, the approximation to the derivative is the same at both points here and were we to work out approximations for the second (or higher) derivatives, using just these two points, they would be zero.

**Example: Three point formulas.**  Suppose we have three equally spaced points $x_0,\,x_1=x_0+h,$ and $x_2=x_0+2h,$ along with the function values at those points $f(x_0),\,f(x_1)$ and $f(x_2)$.   The [formula for the weights](../InterpFit/BarycentricInterp) gives  $w_0= 1/2h^2,\,w_1=-1/h^2$ and $w_2=1/2h^2$.  Using  Eq.{eq}`DLij` and {eq}`DLii` to fill the entries of $\mathbf{D}'$ gives  

$$
\begin{align}
\left[{\begin{array}{c}
f'(x_0) \\
f'(x_1) \\
f'(x_2) 
\end{array}} \right] \approx
\mathbf{D}'\mathbf{F} &=
\left[{\begin{array}{ccc}
  L_0'(x_0) &  L_1'(x_0) & L_2'(x_0)\\
  L_0'(x_1) &  L_1'(x_1) & L_2'(x_1)\\
  L_0'(x_2) &  L_1'(x_2) & L_2'(x_2)
\end{array}} \right]
\left[{\begin{array}{c}
f(x_0) \\
f(x_1) \\
f(x_2)
\end{array}} \right] \\
&=
\left[{\begin{array}{ccc}
  -\frac{3}{2h} & \frac{4}{2h}  & -\frac{1}{2h}\\
  -\frac{1}{2h} & 0  & \frac{1}{2h}\\
  \frac{1}{2h}& -\frac{4}{2h}  & \frac{3}{2h}
\end{array}} \right]
\left[{\begin{array}{c}
f(x_0) \\
f(x_1) \\
f(x_2)
\end{array}} \right] \\
&=
\left[{\begin{array}{c}
\frac{-3f(x_0)+4f(x_1)-f(x_2)}{2h} \\
\frac{f(x_2)-f(x_0)}{2h} \\
\frac{3f(x_2)-4f(x_1)+f(x_0)}{2h}
\end{array}} \right].
\end{align}
$$  

The formula for $x_0$ and $x_1$ are, presumably, higher order (than {eq}`forbackD`) forward/backward differences and the formula for $x_1$ is the *central* difference formula.

With three points, we can also work out approximations for the second derivative.  First, as we have already worked out all the $L_i'(x_j)$, we note that using the formulas for the first derivatives, the second derivative formula in {eq}`DLij` for $i\neq j$ can be rewritten as

$$
\begin{align}
L_i''(x_j)&=-2L_i'(x_j)\left[\sum_{k\neq j}L_k'(x_j)+\frac{1}{x_j-x_i}\right],\\
&= 2L_i'(x_j)\left[L_j'(x_j)-\frac{1}{x_j-x_i}\right].
\end{align}
$$ (DL2fromDL1)

where for the second line we have make use of {eq}`DLii` for the first derivative sum.  Making use of this for the off-diagonal elements and then using {eq}`DLii` for the second derivatives on the diagonal we get

$$
\begin{align}
\left[{\begin{array}{c}
f''(x_0) \\
f''(x_1) \\
f''(x_2) 
\end{array}} \right] \approx
\mathbf{D}''\mathbf{F} &=
\left[{\begin{array}{ccc}
  L_0''(x_0) &  L_1''(x_0) & L_2''(x_0)\\
  L_0''(x_1) &  L_1''(x_1) & L_2''(x_1)\\
  L_0''(x_2) &  L_1''(x_2) & L_2''(x_2)
\end{array}} \right]
\left[{\begin{array}{c}
f(x_0) \\
f(x_1) \\
f(x_2)
\end{array}} \right] \\
&=
\left[{\begin{array}{ccc}
  \frac{1}{h^2} & -\frac{2}{h^2}  & \frac{1}{h^2}\\
  \frac{1}{h^2} & -\frac{2}{h^2}  & \frac{1}{h^2}\\
  \frac{1}{h^2} & -\frac{2}{h^2}  & \frac{1}{h^2}
\end{array}} \right]
\left[{\begin{array}{c}
f(x_0) \\
f(x_1) \\
f(x_2)
\end{array}} \right] \\
&=
\left[{\begin{array}{c}
\frac{f(x_0)-2f(x_1)+f(x_2)}{h^2} \\
\frac{f(x_0)-2f(x_1)+f(x_2)}{h^2} \\
\frac{f(x_0)-2f(x_1)+f(x_2)}{h^2}
\end{array}} \right].
\end{align}
$$  

Not surprisingly as this is based on a single quadratic interpolation, the approximation to the second derivative is the same at all points here and were we to work out approximations for the higher derivatives based on just three points they would all be zero.







