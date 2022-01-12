The problem

When handling affine transformations in 2D with these $3\times3$ matrices, you're embedding the usual 2D plane in 3D as $\left\{ \left.\begin{pmatrix}x\\y\\1\end{pmatrix}\right|x,y\in\mathbb{R}\right\}$, otherwise known as “the plane $z=1$”. The role of the bottom row of an affine transformation matrix $\begin{pmatrix}a_{11} & a_{12} & t_{1}\\a_{21} & a_{22} & t_{2}\\0 & 0 & 1\end{pmatrix}$ is to make sure that a point in the plane $z=1$ is mapped to another point in the same plane. If you were to change the bottom row, you'd usually end up with a point outside of the plane $z=1$, and you probably wouldn't know how to map it back to a point in the usual 2D plane.


Another perspective

However, there is a trick/another way of looking at this situation. You see, the plane $z=1$ has the nice property that every one of its points lies on exactly one line through the origin in 3D, and “most” lines through the origin pass through the plane $z=1$. Moreover, every point in 3D except for the origin lies on exactly one line through the origin, and most of them lie on a line that passes through the plane $z=1$. So what we can usually do, when we have a point not in the plane $z=1$, is follow the line through the origin until we get to the plane $z=1$ and then we know what the corresponding 2D point would be.

Algebraically, if $c\ne0$ and we are considering $\begin{pmatrix}a\\b\\c\end{pmatrix}$, we can divide by $c$ to get $\begin{pmatrix}a/c\\b/c\\1\end{pmatrix}$. That makes it reasonable to associate $\begin{pmatrix}a\\b\\c\end{pmatrix}$ with the 2D point $\left(\dfrac{a}{c},\dfrac{b}{c}\right)$ when $c$ is nonzero. Since they'll represent the same 2D point, I'll use $\sim$ to denote when one triple is a nonzero multiple of another: e.g. $\begin{pmatrix}a\\b\\c\end{pmatrix}\sim\begin{pmatrix}a/c\\b/c\\1\end{pmatrix}$.
Modifying the 1

This immediately allows us to interpret modifications of the $1$ in the lower right corner of the affine transformation matrix. If $\lambda\ne0$, $$\begin{pmatrix}a_{11} & a_{12} & t_{1}\\a_{21} & a_{22} & t_{2}\\0 & 0 &\lambda\end{pmatrix}\begin{pmatrix}x\\y\\1\end{pmatrix}=\lambda\begin{pmatrix}\dfrac{a_{11}}{\lambda} & \dfrac{a_{12}}{\lambda} & \dfrac{t_{1}}{\lambda}\\\dfrac{a_{21}}{\lambda} & \dfrac{a_{22}}{\lambda} & \dfrac{t_{2}}{\lambda}\\0 & 0 & 1\end{pmatrix}\begin{pmatrix}x\\y\\1\end{pmatrix}\sim\begin{pmatrix}\dfrac{a_{11}}{\lambda} & \dfrac{a_{12}}{\lambda} & \dfrac{t_{1}}{\lambda}\\\dfrac{a_{21}}{\lambda} & \dfrac{a_{22}}{\lambda} & \dfrac{t_{2}}{\lambda}\\0 & 0 & 1\end{pmatrix}\begin{pmatrix}x\\y\\1\end{pmatrix}\text{.}$$ Therefore, in our convention for interpreting 3D points, modifying the $1$ just scales the entries that do the affine transformation by a constant amount.
Modifying the 0s

Similarly, we can examine what happens when we modify the $0$s in the bottom row. As a special case, when there is no affine transformation at all, we have $$\begin{pmatrix}1 & 0 & 0\\0 & 1 & 0\\p_{x} & p_{y} & 1\end{pmatrix}\begin{pmatrix}x\\y\\1\end{pmatrix}=\begin{pmatrix}x\\y\\p_{x}x+p_{y}y+1\end{pmatrix}\sim\begin{pmatrix}\dfrac{x}{p_{x}x+p_{y}y+1}\\\dfrac{y}{p_{x}x+p_{y}y+1}\\1\end{pmatrix}$$

The last step is valid for most points, where $p_{x}x+p_{y}y+1\ne0$. Because of this scaling, points that started close to the line $p_{x}x+p_{y}y+1=0$ end up dilated (away from the origin), and points that started far away from the line end up contracted (towards the origin). This is not an affine transformation, but a standard type of “perspective transformation” (sometimes called “perspective projection”).
General Case

In the fully general case, we have the following complicated expression:

$$\begin{pmatrix}a_{11} & a_{12} & t_{1}\\a_{21} & a_{22} & t_{2}\\z_{1} & z_{2} &j\end{pmatrix}\begin{pmatrix}x\\y\\1\end{pmatrix}=\begin{pmatrix}a_{11}x+a_{12}y+t_{1}\\a_{21}x+a_{22}y+t_{2}\\z_{1}x+z_{2}y+j\end{pmatrix}\sim\begin{pmatrix}\dfrac{a_{11}x+a_{12}y+t_{1}}{z_{1}x+z_{2}y+j}\\\dfrac{a_{21}x+a_{22}y+t_{2}}{z_{1}x+z_{2}y+j}\\1\end{pmatrix}$$ The last step is valid where $z_{1}x+z_{2}y+j\ne0$. Because of this scaling, points that started close to the line $z_{1}x+z_{2}y+j=0$ end up dilated after the affine transformation is performed, and points that started far away from the line end up contracted after the affine transformation. For example, $\begin{pmatrix}1 & 0 & -1.9\\0 & 1 & -1.33\\-0.33 & 0.54 & 1.3\end{pmatrix}$ takes a “dog” with many right angles to a warped dog with none (the dashed line is $z_{1}x+z_{2}y+j=0$).




You can explore these sorts of transformations interactively at http://demonstrations.wolfram.com/HomogeneousCoordinatesAndTheProjectivePlane/ . Unfortunately, if you don't have Mathematica, you'll need the Wolfram CDF player which is large and does not work with Chrome (but should work with Firefox, I believe).
Assorted Side Notes

- If $j\ne0$, note that: $$\begin{pmatrix}\dfrac{a_{11}x+a_{12}y+t_{1}}{z_{1}x+z_{2}y+j}\\\dfrac{a_{21}x+a_{22}y+t_{2}}{z_{1}x+z_{2}y+j}\\1\end{pmatrix}=\left(\dfrac{1}{j}\begin{pmatrix}a_{11} & a_{12} & t_{1}\\a_{21} & a_{22} & t_{2}\\z_{1} & z_{2} & j\end{pmatrix}\right)\begin{pmatrix}x\\y\\1\end{pmatrix}$$ so nearly all possible “generalized affine transformations” of this form can use a $1$ in the lower right entry, if we like.
- All of the above discussion extends just fine to higher dimensions, and it's in fact used often in computer graphics calculations one dimension higher (See, for example, http://www.scratchapixel.com/lessons/3d-basic-rendering/perspective-and-orthographic-projection-matrix/building-basic-perspective-projection-matrix ).
- Finally, there's a lot of beautiful mathematics involved in not throwing away the points $\begin{pmatrix}a\\b\\0\end{pmatrix}$. They're kind of like “points infinitely far from the origin where parallel lines can meet”. You get the “real projective plane”, sometimes called the “extended Euclidean plane”. The sorts of coordinates we're using where we don't care about multiples are called “homogeneous coordinates” in general.
