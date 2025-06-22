#lang racket
(define (largo x [n 0])
    (if (null? x) 
        n
        (largo (cdr x) (+ n 1))
    )
)

(largo '(a b c))
(largo '())
(largo '(a))