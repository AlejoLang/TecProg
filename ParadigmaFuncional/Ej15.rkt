#lang racket

(define (primer-num (l1 '()))
    (if (null? l1)
        null
        (if (number? (car l1))
            (car l1) 
            (primer-num (cdr l1))
        ) 
    )
)

(primer-num '('(1 . 3) 'a '(b)  'a ))