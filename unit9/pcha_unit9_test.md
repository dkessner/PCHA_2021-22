__Unit 9 Test__  
__PCHA 2021-22 / Dr. Kessner__  

\vspace{.2in}

__Name / Pledge:__

\vspace{.2in}

__No calculator!  Have fun!__

\vspace{.2in}

\let\svlim\lim\def\lim{\displaystyle\svlim}

__1.__ Evaluate the following limits, evaluating left and right side limits
where applicable.  

\vspace{.2in}

Let $f(x) = \dfrac{x-3}{(x-2)(x-3)}$

\vspace{.2in}

a. $\lim_{x \to \infty} f(x)$

\vspace{1in}

b. $\lim_{x \to 2} f(x)$

\vspace{1in}

c. $\lim_{x \to 3} f(x)$

\vspace{1in}

d. $\lim_{x \to 0} (-\csc x)$

\vspace{1in}

e. $\lim_{x \to \frac{3\pi}{2}} \dfrac{\sin x - \sin \frac{3\pi}{2}}{x-\frac{3\pi}{2}}$

\newpage

__2.__  a. Let $g(x) = 5x^3 + x$.  Find $g'(x)$ using a limit definition.

\vspace{3in}

b. A little bird whispers to you:  For any $a$,
$$
    \lim_{x \to 0} \dfrac{a^x - 1}{x} = \ln a
$$

    Let $f(x) = 2^{x}$.  Find $f'(x)$ using a limit definition and the ancient knowledge
    you have gained from the bird.  

\newpage

__3.__ Calculate the derivatives of the following functions.

a. $r(x) = x^3 + 3^x + x^{-3}$

\vspace{1.25in}

b. $s(x) = \log_2 \sin x$

\vspace{1.25in}

c. $t(x) = \sec ^2 x$

\vspace{1.25in}

d. $t(x) = \sec ^2 x = \dfrac{1}{\cos ^2 x}$ using the quotient rule:
$$
    \left(\dfrac{f}{g}\right)'(x) = \dfrac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}
$$

\vspace{1.25in}

e. $t(x) = \sec^2 x = (\cos x)^{-2}$ using the product, power, and
chain rules.

\newpage

__4.__  a. Let $y = \sqrt[4]{x}$.  Find $\dfrac{dy}{dx}$ in two ways: 1)
the general power rule,  2) implicit differentiation (plus the integer power
rule).  Verify that your answers are the same.

\vspace{4in}



b.  Let $y = \tan^{-1}x$ (inverse $\tan$, not reciprocal).
Use implicit differentiation to show that: 
$$ \dfrac{dy}{dx} = \dfrac{1}{1 + x^2} $$

\vspace{2in}

c. Let $c(x) = \tan^{-1} (\tan x)$.  

    Use the formula above and the chain rule to find $c'(x)$.


\newpage

__5.__  You are quarantined at home and bored, contemplating a
clock on your wall.  Suppose the minute hand of the clock is 6
inches long.  (What is the period in minutes?)

a.  Let the origin be the center of the clock.  Find parametric
equations for the position of the tip of the minute hand.  For
example, at t=0, the position is $(0,6)$, and at t=15 minutes, the
position is $(6,0)$.  

\vspace{2in}

b.  Find equations for $x'(t)$ and $y'(t)$.

\vspace{1.5in}

c.  The _speed_ is the magnitude of the velocity vector $\left<x'(t),
y'(t)\right>$.  Show that the speed of the tip of the hour hand is
$\dfrac{12\pi}{60}$.  __Bonus:__ Explain why this makes sense.

\vspace{1.5in}

d.  Let $s(t) = \dfrac{y(t)}{x(t)}$ be the slope of the minute hand (as a line).
Find $s(t)$ and $s'(t)$ at $t=0, 15, 30, 45$ minutes.

\newpage

__Bonus__  Assuming the differentiation rule for $a^x$, derive (!) the
differentiation rule for $\log_a x$.


\vspace{4in}

__Bonus__ Derive the general power rule for derivatives: $\dfrac{d}{dx}x^r =
rx^{r-1}$ for any $r \in \mathbb{R}$.  _Hint:_ Let $y = x^r$.  Take the natural
log of both sides, and use implicit differentiation.

\newpage

__Bonus__  Show that the vertex of the parabola $y = ax^2 + bx + c$ is located
at $x=\frac{-b}{2a}$.

\vspace{4in}

__Bonus__ Parametrize a circle of radius 6 around the origin.  Show that the
position vector $\left<x(t), y(t)\right>$ is always orthogonal to the velocity
vector $\left<x'(t), y'(t)\right>$, and that the velocity vector is orthogonal to the
acceleration vector.

\newpage

__Bonus__ 

\vspace{-1.5in}

![](polygon.pdf){width=6in}

\vspace{-5in}

Let $P(n)$ be the perimeter of the regular $n$-sided polygon inscribed in the
unit circle. Show that
$$
    P(n) = n \cdot 2\sin(\frac{2\pi}{2n}) = 2n\sin(\frac{\pi}{n})
$$

\vspace{3in}

Show that
$$
    \lim_{n \to \infty} P(n) = 2\pi
$$
_Hint_: Let $x=\frac{1}{n}$.  Why does this make sense?

\newpage


---
pagetitle: none
math: <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_CHTML-full" type="text/javascript"></script> 
geometry: margin=1in
---


