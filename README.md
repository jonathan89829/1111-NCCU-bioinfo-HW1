# hw1

## Description

* Writing R/Python program to generate PAM<sub>x</sub> from the given mutation probability matrix.
* PAM<sub>x</sub> must be as a log odds and complete square matrix (rounding to integer), not the format of the given mutation probability matrix.
* Creating your own program, ie. hw1_105753026.R, to read mut.txt and *x*, then output pamx.txt.
* [HINT] PAM<sub>x</sub> is a symmetric matrix even the given mutation probability matrix is not.
* [HINT] The mutation matrix should be divided by 10,000 before calculation PAM250, the value in matrix should be in [0,1].

## File

* hw1_ref.R: You can start from this reference code, and try to write your own comment in English
* mut.txt: the mutation probability matrix, M<sub>1</sub>

## Command

Executing your code with the following command.
ie.

```R
Rscript hw1_studentID.R --input input_path_mut.txt --pam x --output output_path_pamx.txt
```

## Evaluation
* works for input & output right PAM<sub>250</sub>: 80
* support input, pam, output options: 85
* allow shuffle option order: 90

### Bonus

* Preprocess PAM<sub>1</sub>: +2
* Post-process PAM<sub>250</sub>: +2
* Correct output format: +2
* Output without quotation marks "": +2
* Round to the nearest integer number: +2

### Penalty

* Use the fixed path inside your code: -1
* Calculate with the wrong number of loops: -1
* High code similarity to others: YOUR SCORE = 0
