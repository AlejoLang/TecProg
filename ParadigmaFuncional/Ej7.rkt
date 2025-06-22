#lang racket

(define (mascorta x y)
    (if (> (length x) (length y))
        y
        x)
    x
)

(mascorta '(a b) '(a b c d))
(mascorta '(a c) '(c d))