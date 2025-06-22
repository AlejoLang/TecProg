#lang racket

(define (attach-at-end (v null) (l '()))
    (if (null? v)
        l
        (if (null? l)
            (list v) 
            (cons (car l) (attach-at-end v (cdr l)))
        ) 
    )
)

(attach-at-end 'palabra '(esto es una))