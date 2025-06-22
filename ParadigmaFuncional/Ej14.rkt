#lang racket

(define (concatenar (l1 '()) (l2 '()))
    (if (null? l1)
        l2
        (if (null? (cdr l1))
            (cons (car l1) l2)
            (cons (car l1) (concatenar (cdr l1) l2))
        )
    )
)

(concatenar (list 1 2 3) (list 4 5 6))
(concatenar (list ) (list 1 2 3))
(concatenar (list 1 2 3) (list ))