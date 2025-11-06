---
puppeteer:
  format: "A4"
  
  displayHeaderFooter: true
  headerTemplate: ' '
  footerTemplate: >
    <div style="font-size: 14px; width: 100%; text-align: center; padding: 0 1cm;">
      <span class="pageNumber"></span> / <span class="totalPages"></span>
    </div>
id: "test"
---
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script>
document.addEventListener("DOMContentLoaded", function() {
  renderMathInElement(document.body, {
    delimiters: [
      {left: "$$", right: "$$", display: true},
      {left: "$", right: "$", display: false}
    ],
    throwOnError: false
  });
});
</script>
</head>
<body>
</body>
</html>

<div class="cover-page">
  <div class="cover-main-title">
    Calculus
  </div>
  <div class="cover-subtitle">
    HW3:Understanding Limit/Continuity and Crystal Growth Limit Obsrvation
  </div>
  <div class="cover-group">
    組別：第15組
  </div>
  <div class="cover-authors">
    組員：<br>
    411485018 蘇星丞<br>
    411485002 楊昕展<br>
    411485003 胡庭睿<br>
    411485042 黃柏崴
  </div>
</div>



# Basic Concepts for Limits

## Q1
Evaluate the limit and justify each step by indicating the appropriate Limit Law(s)
1. $\lim_{x \to -3} (2x^3+ 6x^2 - 9)$
2. $\lim_{x \to 3} \sqrt[3]{x + 5}{(2x^2 - 3x)}$

## Ans1

1. 
$$
\begin{aligned}
&\lim_{x \to -3} (2x^3 + 6x^2 - 9) \\
&= \lim_{x \to -3} (2x^3) + \lim_{x \to -3} (6x^2) - \lim_{x \to -3} (9) && \text{(Sum/Difference Law)} \\
&= 2 \lim_{x \to -3} (x^3) + 6 \lim_{x \to -3} (x^2) - \lim_{x \to -3} (9) && \text{(Constant Multiple Law)} \\
&= 2(\lim_{x \to -3}x)^3+6(\lim_{x \to -3}x)^2-(\lim_{x \to -3}9) && \text{(Power Law)}\\
&= 2(-3)^3 + 6(-3)^2 - 9 && \text{(Appendix A 8,10)} \\
&= 2(-27) + 6(9) - 9 \\
&= -54 + 54 - 9 \\
&= -9
\end{aligned}
$$

2. 
$$
\begin{aligned}
&\lim_{x \to 3} \sqrt[3]{x + 5}{(2x^2 - 3x)} \\
&= \sqrt[3] {\lim_{x \to 3}(x+5)} \times \lim_{x \to 3}(2x^2-3x) &&\text{(Root / Product Law)}\\
&= \sqrt[3] {\lim_{x \to 3}(x+5)} \times (2\lim_{x \to 3}x^2 - 3\lim_{x \to 3}x) &&\text{(Sum / Difference / Constant Multiple Law)}\\
&= \sqrt[3]8 \times (2 \times 3^2-3\times3) &&\text{(Power Law)}\\
&= 2 \times 9\\
&=18
\end{aligned}
$$

***

## Q2
Evaluate the limit, if it exists.
1. $\lim_{x \to -2}(3x-7)$

2. $\lim_{t^2-2t-8}(t-4)$

3. $\lim_{x \to 2}\frac{2-x}{\sqrt{x+2}-2}$

4. $\lim_{x \to 3} \frac{\frac{1}{x} - \frac{1}{3}}{x-3}$

## Ans2

1. Because $3x-7$ is a continuous function, which means $\lim_{x \to 2}3x-7 = 3\times 2-7(\text{continuous definition:}\lim_{x \to a}f(x) = f(a))$,so we can find out that the limit is $-1$

2. The limit expression is mathematically ill-defined. The notation below $\lim$ ,which is $t^2-2t-8$,is not a valid convergence condition. It fails to specify the value that the variable t is approaching (ex:$t \to 4$). Without this "target point," the limit cannot be calculated, so this problem has no solution.

3. We cannot apply Quotient Law because the limit of the denominator is 0, so we need to perform algebraic simplification on the expression first.
$$
\begin{aligned}
&\lim_{x \to 2}\frac{2-x}{\sqrt{x+2}-2} \times \frac{\sqrt{x+2}+2}{\sqrt{x+2}+2} \\
&= \lim_{x \to 2}\frac{(2-x)(\sqrt{x+2}+2)}{(\sqrt{x+2})^2-4} \\
&= \lim_{x \to 2}\frac{(2-x)(\sqrt{x+2}+2)}{x+2-4} \\
&= \lim_{x \to 2}\frac{(2-x)(\sqrt{x+2}+2)}{x-2} \\
&= \lim_{x \to 2}\frac{-(x-2)(\sqrt{x+2}+2)}{x-2} && \text{(Cancel x-2)}\\
&= \lim_{x \to 2}-(\sqrt{x+2}+2)  \\
&= -(\sqrt{2+2}+2) \\
&= -(2+2) \\
&= -4
\end{aligned}
$$


4. Same as the last question, because the limit of the denominator is 0, so we need to perform algebraic simplification on the expression first.

$$
\begin{aligned}
&\lim_{x \to 3} \frac{\frac{1}{x} - \frac{1}{3}}{x-3} \times \frac{x+3}{x+3}\\
&= \lim_{x \to 3}\frac{\frac{3}{x}-\frac{x}{3}}{x^2-9}\\
&= \lim_{x \to 3}\frac{\frac{1}{3x}(9-x^2)}{x^2-9} &&\text{(Cancel } x^2-9 \text{)}\\
&= \lim_{x \to 3} \frac{1}{3x}\times-1 \\
&= \frac{1}{9}\times -1\\
&= \frac{-1}{9}
\end{aligned}
$$



***
 

## Q3
Use Squeeze Theeorom to show that 
$$\lim_{x \to 0}\sqrt{x^3+x^2}\sin{\frac{\pi}{x}}$$
## Ans3
$$ -1\leq\sin{\frac{\pi}{x}}\leq1\\$$
$$-\sqrt{x^3+x^2}\leq\sqrt{x^3+x^2}\sin{\frac{\pi}{x}}\leq\sqrt{x^3+x^2}$$
$$\lim_{x\to 0}-\sqrt{x^3+x^2}\leq\lim_{x\to 0}\sqrt{x^3+x^2}\sin{\frac{\pi}{x}}\leq\lim_{x\to0}\sqrt{x^3+x^2}$$
$$0\leq\lim_{x\to 0}\sqrt{x^3+x^2}\sin{\frac{\pi}{x}}\leq0$$
$$\lim_{x\to 0}\sqrt{x^3+x^2}\sin{\frac{\pi}{x}} = 0$$


***

## Q4
 The figure shows a fixed circle $C_1$ with equation $(x-1)^2 + y^2 = 1$ and a shrinking circle $C_2$ with radius $r$ and centering the origin
- Point $P(0,r)$
- Point $Q$ is the upper intersection point of the two circles
- Point $R$ is where line $PQ$ intersects the x-axis

What happens to point $R$ as circle $C_2$ shrinks (as $r \to 0^+$)?

![Circle Intersection Problem](images/q3.jpeg)
## Ans4
$$
\begin{aligned}
&x^2+y^2=r^2 \hspace{1cm} \text{(1)} \\
&(x-1)^2+y^2=1 \hspace{1cm} \text{(2)} \\
&\text{(1) - (2) cancel } y^2\\
&=2x-1=r^2-1\\
&x=\frac{r^2}{2}\hspace{1cm}y=\frac{r^2}{2}\\
&Q(x, y)=(\frac{r^2}{2}, \frac{r^2}{2})\\
&P(0,r)\\
\end{aligned}
$$
Find the slope $m_{\overline{PQ}} = 1-\frac{2}{r}$ 
Use P to find the equation of the line $L_{\overline{PQ}}=(1-\frac{2}{r})x =(y-r) $
so $R$ is fix on $x$ axias and to find $R$ we assume $R=R(k,0)$ 
plug in line L which gives us the equation equation$(1-\frac{2}{r})k =-r$ then simplify the equation and we will get the new equation $k = - \frac{r^2}{r-2}$

$$\lim_{r \to 0^+}k = \lim_{r \to 0^+}-\frac{r^2}{r-2} = 0$$
so as $r \to 0^+$ $\hspace{0.5cm}$ $R(k,0)\to (0,0)$



***

## Q5
Use the given graph of $f$ to find a number $\delta$ such that:

- $0 < |x - 3| < \delta$ implies $|f(x) - 2| < 0.5$

$$
0 < |x - 3| < \delta \implies |f(x) - 2| < 0.5
$$

![Graph for Q5](images/q4.jpeg)


## Ans5
$$
\begin{aligned}
&|f(x)-2| < 0.5\\
&1.5 < f(x) < 2.5\
&f(x)=1.5\hspace{0.2cm}\text{as}\hspace{0.2cm}x = 2.6\\
&f(x)=2.5\hspace{0.2cm}\text{as}\hspace{0.2cm}x = 3.8\\
\end{aligned}
$$
so when $x \in(2.6,3.8)$ then the inequality $|f(x) - 2| < 0.5$ will be satisfied
Given the inequality $0<|x-3|<\delta$ , the value of $\delta$  must ensure that the condition $|f(x)-2|<0.5$ is satisfied.
This means $\delta$  must be the smallest distance between 3 and the x-values where $f(x)=1.5$ and $f(x)=2.5$, which are 2.6 and 3.8 respectively.
Therefore, $\delta =\min (3-2.6,\  3.8-3)=\min (0.4,\  0.8)=0.4$.


***

## Q6

## Ans6

***

## Q7

## Ans7

***

## Q8

## Ans8


<!-- pagebreak -->

# Basic Concepts for Continuity

## Q1
Prove that $f$ is continuous at $a$ if and only if
$$ \lim_{h \to 0} f(a + h) = f(a) $$

## Ans1
Prove: $f$ is continuous at $a$  $\iff \lim_{h \to 0} f(a + h) = f(a)$

From class's slides, we know that the definition of continuous is $\lim_{x \to a}f(x) = f(a)$

### Part 1 : Foward direction's proof
Assume f is continuous at a, we know by the definition of continuous $\lim_{x \to a}f(x) = f(a)$.

Define a variable h , and set $x = a + h$, when $x$ $\to$ $a$, $h \to 0$

Now we can replace $x$ with $a+h$ and the limit condition $x \to a$ with $h \to 0$
$$\lim_{h \to 0}f(a+h) = f(a)$$

From above, it have proven that if $f$ is continuous at $a$, then the given limit expression holds true.

### Part 2 : Reverse direction's proof

Assume $\lim_{h \to 0} f(a + h) = f(a)$, and we want to prove f is continuous at a

According to above, we define $x = a+h$, which means $h = x-a$

As $h \to 0$, the value of $x$$\text{(a+h)}$ must approach $a+0$, so we can know as $h \to 0$,then $x \to a$

Now we can replace $h$ with $x-a$ and the limit condition $h \to 0$ with $x \to a$
  $$ \lim_{x \to a} f(a + (x - a)) = f(a) $$
After simplify:
$$ \lim_{x \to a} f(x) = f(a) $$

From above, it have proven that if $\lim_{h \to 0} f(a + h) = f(a)$ is true, f is continuous at a.

### Conclusion
Since we have proven the statement in both directions , we have successfully shown that a function f is continuous at a if and only if $\lim_{h \to 0} f(a + h) = f(a)$.

***

## Q2
The graph of a function f is given.
![](images/q2.png)

1. At what numbers a does $\lim_{x \to a}f(x)$ not exist?

2. At what numbers a is f not continuous?

3. At what numbers a does  $\lim_{x \to a}f(x)$ exist but f is not continuous at a?

## Ans2
* The criteria for limits, continuity, and differentiability can be found in Appendix B

1. $x=1$, because $lim_{x\to 1-}f(x) \neq lim_{x\to 1+}f(x)$ 

2. $x=3$, because $\lim_{x\to 3}f(x) \neq f(3)$

3. $x=3$, according to Appendix B, although left-hand limit equals to right-hand limit and both exist(conditions for the existence of a limit), $\lim_{x\to 3}f(x) \neq f(3)$, from above we can know that $f$ is not continuous at $a$.

***

## Q3

## Ans3

***

## Q4

## Ans4



<!-- pagebreak -->

# Crystal Growth Inspection

## ?.py

```python

```

***

## ?2.py

```python


```




# Work Division

| 學號/姓名 | 分配項目（寫） | 分配項目（檢查） |
| --- | --- | --- |
| 411485002 楊昕展 |   |   |
| 411485003 胡庭睿 | part 1:1,2<br> part 2:1,2<br> Appendix A,B|   |
| 411485018 蘇星丞 |   |   |
| 411485042 黃柏崴 |   |   |


# Challenges and Difficulties
 
### 姓名：胡庭睿
### 遇到的困難與挑戰：
1. markdown轉pdf
在上次作業中使用的extension(markdown pdf)，在轉換多行latex公式時(ex: \begin{aligned})會無法辨別，於是我在網上尋找許多不同方法，但是轉換的效果都不令我滿意，pandoc雖然能夠很好的渲染出latex公式，但是圖片的位置卻無法置中，換了很多個latex engine依然無解(pdflatex, mactex, xetex)再加上標題頁是用html寫的， 也意味著標題頁需要重寫，但是我卻一直無法將它修改到我想要的樣式，最後我找到了一個叫做markdown preview enhanced

2. latex撰寫作業
3. 全英文撰寫作業
***

### 姓名： 
### 遇到的困難與挑戰：

***

### 姓名： 
### 遇到的困難與挑戰：

***

### 姓名： 
### 遇到的困難與挑戰：

# Meeting Records

| 會議日期 | 會議方式 (線上/實體) | 討論事項 |
| :--- | :--- | :--- |
| [日期] | [方式] | 1. 作業要求釐清<br>2. 進度規劃<br>3. 問題整合<br>4. 角色分配討論 |
| ... | ... | ... |
| ... | ... | ... |

# Working Hours Records

| 組員姓名 | 工作時數 | 工作項目 | 工時高/低原因分析 (Bonus) |
| :--- | :--- | :--- | :--- |
| 胡庭睿 | 15hr | 1. part 1:1,2<br> 2. part 2:1,2<br> 3. Appendix A,B<br> 4. the homework template<br> 5. git and github tutorial<br>6. find ways of converting markdown to pdf |
| [姓名2] | [時數] | 1. [工作項目1]<br>2. [工作項目2] | [自行分析原因] |
| ... | ... | ... | ... |


# Reflection

### 學號：
### 姓名：
### 心得：


***

### 學號：
### 姓名：
### 心得：

***

### 學號：
### 姓名：
### 心得：

***

### 學號：
### 姓名：
### 心得：

# Appendix


## Appendix A

### Limit Laws in class's slides:
1. Sum Law $\text{ (} \lim_{x \to a}(f(x)+g(x)) = \lim_{x \to a}f(x) + \lim_{x \to a}g(x) \text{)}$

2. Difference Law $\text{ (} \lim_{x \to a}(f(x)-g(x)) = \lim_{x \to a}f(x) - \lim_{x \to a}g(x) \text{)}$

3. Constant Multiple Law $\text{ (} \lim_{x \to a}cf(x) = c\times \lim_{x \to a}f(x) \text{)}$

4. Product Law $\text{ (} \lim_{x \to a}(f(x)g(x)) = \lim_{x \to a}f(x) \times \lim_{x \to a}g(x) \text{)}$

5. Quotient Law $\text{ (} \lim_{x\to a}\frac{f(x)}{g(x)}=\frac{\lim_{x\to a}f(x)}{\lim_{x\to a}g(x)}\text{, if }\lim_{x\to a}g(x)\neq 0\text{)}$

6. Power Law $\text{ (} \lim_{x \to a}(f(x)^n)) = (\lim_{x \to a}f(x))^n\text{)}$

7. Root Law $\text{ (} \lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{\lim_{x \to a}f(x)} \text{)}$

8. $\lim_{x\to a}c = c \text{  (c為常數)}$

9. $\lim_{x \to a}x = a$

10. $\lim_{x \to a}x^n = a^n$

11. $\lim_{x \to a}\sqrt[n]{x} = \sqrt[n]{a}$

## Appendix B

### 極限存在條件
1. $\lim_{x \to a-}f(x) $ 存在

2. $\lim_{x \to a+}f(x) $ 存在

3. $\lim_{x \to a-}f(x) = \lim_{x \to a+}f(x)$

### 在點a連續條件
1. $f(a)$ 存在

2. $\lim_{x \to a}f(x)$ 存在

3. $\lim_{x \to a}f(x) = f(a)$

### 在點a可微分條件
1. $f(a)$ 存在

2. $f(x)$ is continuous at $a$

3. $\lim_{x \to a-}\frac{f(x)-f(a)}{x-a}$ 存在

4. $\lim_{x \to a+}\frac{f(x)-f(a)}{x-a}$ 存在

5. $\lim_{x \to a-}\frac{f(x)-f(a)}{x-a} = \lim_{x \to a+}\frac{f(x)-f(a)}{x-a} $ 

### 三者關係
可微分一定連續，若連續，極限一定存在
## Appendix C