---
puppeteer:
  format: "A4"
  margin:
    top: "2cm"
    bottom: "2cm"
  output:
    pdf_document:
      latex_engine: "pdflatex"
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
<style>
  .cover-page {
    page-break-after: always;
    text-align: center;
    padding-top: 30vh;
  }
  .cover-main-title {
    font-size: 48px;
    font-weight: bold;
    margin-bottom: 30px;
    line-height: 1.5;
  }
  .cover-subtitle {
    font-size: 24px;
    color: #000000ff;
    margin-bottom: 60px;
    line-height: 1.6;
  }
  .cover-group {
    font-size: 18px;
    color: #00000000;
    margin-bottom: 40px;
  }
  .cover-authors {
    font-size: 18px;
    color: #000000ff;
    line-height: 2;
  }
</style>
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
$
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
$

2. 
$
\begin{aligned}
&\lim_{x \to 3} \sqrt[3]{x + 5}{(2x^2 - 3x)} \\
&= \sqrt[3] {\lim_{x \to 3}(x+5)} \times \lim_{x \to 3}(2x^2-3x) &&\text{(Root / Product Law)}\\
&= \sqrt[3] {\lim_{x \to 3}(x+5)} \times (2\lim_{x \to 3}x^2 - 3\lim_{x \to 3}x) &&\text{(Sum / Difference / Constant Multiple Law)}\\
&= \sqrt[3]8 \times (2 \times 3^2-3\times3) &&\text{(Power Law)}\\
&= 2 \times 9\\
&=18
\end{aligned}
$

---

## Q2
Evaluate the limit, if it exists.
1. $\lim_{x \to -2}(3x-7)$
2. $\lim_{t^2-2t-8}(t-4)$
3. $\lim_{x \to 2}\frac{2-x}{\sqrt{x+2}-2}$
4. $\lim_{x \to 3} \frac{\frac{1}{x} - \frac{1}{3}}{x-3}$
## Ans2

1. Because $3x-7$ is a continuous function, which means $\lim_{x \to 2}3x-7 = 3\times 2-7(\text{continuous definition:}\lim_{x \to a}f(x) = f(a))$,so we can find out that the limit is $-1$
2. The limit expression is mathematically ill-defined. The notation below $\lim$ ,which is $t^2-2t-8$,is not a valid convergence condition. It fails to specify the value that the variable t is approaching (ex:$t \to 4$). Without this "target point," the limit cannot be calculated, so this problem has no solution.
3. 



---
 
## Q3

## Ans3
---

## Q4

## Ans4

---

## Q5

## Ans5

---

## Q6

## Ans6
---

## Q7

## Ans7
---

## Q8

## Ans8



# Basic Concepts for Continuity

## Q1
Prove that f is continuous at a if and only if
$$ \lim_{h \to 0} f(a + h) = f(a) $$

## Ans1

---

## Q2
The graph of a function f is given.
![](images/q2.png)

1. At what numbers a does $\lim_{x \to a}f(x)$ not exist?
2. At what numbers a is f not continuous?
3. At what numbers a does  $\lim_{x \to a}f(x)$ exist but f is not continuous at a?
## Ans2

---

## Q3

## Ans3

---

## Q4

## Ans4

---

# Crystal Growth Inspection

## ?.py

```python

```

---

## ?2.py

```python


```




# Work Division

| 學號/姓名 | 分配項目（寫） | 分配項目（檢查） |
| --- | --- | --- |
| 411485002 楊昕展 |   |   |
| 411485003 胡庭睿 |   |   |
| 411485018 蘇星丞 |   |   |
| 411485042 黃柏崴 |   |   |


# Challenges and Difficulties

此處由每位成員報告在擔任實作者或審核者時遇到的挑戰或未解決的問題，包含未來工作
 
### 姓名： 
### 遇到的困難與挑戰：

---
### 姓名： 
### 遇到的困難與挑戰：

---
### 姓名： 
### 遇到的困難與挑戰：

---
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
| [姓名1] | [時數] | 1. [工作項目1]<br>2. [工作項目2] | [自行分析原因] |
| [姓名2] | [時數] | 1. [工作項目1]<br>2. [工作項目2] | [自行分析原因] |
| ... | ... | ... | ... |


# Reflection

### 學號：
### 姓名：
### 心得：
（應包含在作業中學習到的知識點，個人和小組整題的學習，工作風格的反思，總結在此次作業中遇到的挑戰和問題(work hours, division)）

---
### 學號：
### 姓名：
### 心得：

---
### 學號：
### 姓名：
### 心得：

---
### 學號：
### 姓名：
### 心得：

# Appendix

(可以放聊天記錄，截圖和參考資料)
## Appendix A
### Limit Laws in class's slides:
1. Sum Law (先加再微分 = 先各自微分再相加)
2. Difference Law (先減再微分 = 先各自微分再相減)
3. Constant Multiple Law (若函式可以提出一個常數，先將提出常數後的函數微分再與提出的常數相乘，結果等於原本函式的微分)
4. Product Law (先乘再微分 = 先各自微分再相乘)
5. Quotient Law ()
6. Power Law ()
7. Root Law ()
8. $\lim_{x\to a}c = c \text{(c為常數)}$
9. $\lim_{x \to a}x = a$
10. $\lim_{x \to a}x^n = a^n$
11. $\lim_{x \to a}\sqrt[n]x = \sqrt[n]a$

## Appendix B

## Appendix C