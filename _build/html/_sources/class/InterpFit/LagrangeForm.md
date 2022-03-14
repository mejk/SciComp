## Lagrange Form of the Interpolation Polynomial

The *Lagrange form* of the interpolating polynomial was first formulated by Edward Waring in 1779 (Sadly misattribution of scientific results is probably closer to the norm than it should be.  Attempting to correct misattribution later can be next to impossible once a name has become firmly established).  For centuries the Lagrange form was used primarily as a theoretical tool to help prove mathematical results and build intuition as it has a straightforward analytic form.   Until fairly recently it was thought that changing the points $x_i$ required recalculating the entire interpolant and that evaluating the interpolant was rather inefficient.  However, it is now known that a slight variant, namely barycentric Lagrange interpolation, solves these problems rather straightforwardly.  

To first step in constructing the Lagrange interpolating polynomial is to consider the basis polynomials:

Given $x_0, x_1, ...,x_n$ the **Lagrange basis polynomials** for these points are  

$$
\begin{align}
L_i^n(x)&=\prod_{j=0,j\neq i}^n \frac{(x-x_j)}{(x_i-x_j)},\qquad\qquad i=0,...n\\
&= \frac{(x-x_0)(x-x_1)...(x-x_{i-1})(x-x_{i+1})...(x-x_n)}{(x_i-x_0)(x_i-x_1)...(x_i-x_{i-1})(x_i-x_{i+1})...(x_i-x_n)}.
\end{align}
$$  

The key property of these polynomials is that when evaluated at one of our interpolation points,

$$
\begin{equation}
L_i^n(x_k)=\delta_{ki} = 
\begin{cases}
1, &  \text{if}\, k=i  \\
0, &  \text{if}\, k\neq i
\end{cases}
\end{equation}
$$

If we have 4 points $n=3$ and if the points are equally spaced the Lagrange basis polynomials look like the following:  

[plot of $L_n^j(x)$](./img/lagrangebasis.svg)  

Examining $L_2^3(x)$, for example, we see it is indeed 0 at $x_0,\,x_1,$ and $x_3$ but is 1 at $x_2$.  Also note that all of these are cubic polynomials (degree 3 when we have 4 interpolation points).

The *Lagrange form of the interpoloating polynomial* given data values $(x_0,f(x_0)), (x_1,f(x_1)), (x_2,f(x_2)),..., (x_n,f(x_n))$ is now

$$p_n(x)=\sum_{i=0}^n L_i^n(x) f(x_i)$$

Keep in mind that the $f(x_i)$ is given (i.e. is a number) and so this is a sum over the Lagrange basis polynomials.  By construction

$$\begin{align}
p_n(x_j) &= \sum_{i=0}^n L_i^n(x_j) f(x_i) \\
 &= \delta_{ij} f(x_i) \\
 &= f(x_j).
 \end{align}
$$

So $p_n(x)$ is an interpolating polynomial of degree $\leq n$ through the specifed points, as desired.

Any important question to ask is whether **our interpolating polynomial $p_n(x)$ is unique**.  If not, we would need to decide which one was "best" and perhaps this answer would depend on the circumstance.  Fortunately we can show that our interpolating polynomial *is* unique.

How?  Suppose not, then there is another polynomial, which we will call $q_n(x)$ of degree $\leq n$ with $q_n(x_i)=f(x_i)$ for all $i$ and where for general $x$ we have $p_n(x)\neq q_n(x)$.  Now consider  

$$d_n(x)=p_n(x)-q_n(x),$$

which is another polynomial of degree $\leq n$.  Now if both $p_n(x)$ and $q_n(x)$ are interpolating polynomials through our $n+1$ points we must have

$$d_n(x_i) = p_n(x_i) - q_n(x_i) = f(x_i)- f(x_i) = 0, \qquad\qquad i=0,1,...,n$$

which means $d_n(x_i)$ has $n+1$ roots (or zeros).  However, the fundamental theorm of algebra tells us that a $n-$degree polynomial has at most $n$ roots.  The only way to resolve this contradiction is if $d_n(x)\equiv 0$ implying that $q_n(x)\equiv p_n(x)$ so that the polynomial is unique.

Note that while the polynomial is unique, we are free to rearrange it algebraically to construct a different form of the same polynomial. Why would you want to do this?

1. $L_j^n(x)$ is a $n$'th degree polynomial and so requires $\mathcal{O}(n)$ flops (we discussed this in conjunction with Horner's algorithm in an earlier chapter).  We have $n+1$ of these to compute so direct use of the Lagrange form of $p_n(x)$ would require $\mathcal{O}(n^2)$ flops.  This is inefficient for a polynomial that is still of degree $n$.

2. If we decide to change or add another node at $x_k$ it would appear that all the Lagrange basis polynomials would have to be recalculated.

It is for these reasons that Lagrange interpolating polynomials had limited practical (as opposed to theoretical) application for many years.  However, these problems can be easily fixed as we discuss next.
